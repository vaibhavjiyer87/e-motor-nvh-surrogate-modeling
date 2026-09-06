"""
P02 physics-guided feature implementation.

Specification:
    P02-FEAT-001 v001

Features are calculated from UNSCALED RMS currents.
No target information or scaling is used here.
"""

import numpy as np
import pandas as pd


FEATURE_EPSILON_A = 1e-6


CURRENT_COLUMNS = [
    "Currents_Sub1[1].rms",
    "Currents_Sub1[2].rms",
    "Currents_Sub1[3].rms",
    "Currents_Sub2[1].rms",
    "Currents_Sub2[2].rms",
    "Currents_Sub2[3].rms",
]


RAW_7 = CURRENT_COLUMNS + ["Speed_mech"]


DERIVED_13 = [
    "sub1_mean_rms",
    "sub2_mean_rms",

    "sub1_phase_imbalance",
    "sub2_phase_imbalance",

    "cross_phase1_signed_diff_rms",
    "cross_phase2_signed_diff_rms",
    "cross_phase3_signed_diff_rms",

    "cross_phase1_abs_diff_rms",
    "cross_phase2_abs_diff_rms",
    "cross_phase3_abs_diff_rms",

    "cross_phase1_log_ratio",
    "cross_phase2_log_ratio",
    "cross_phase3_log_ratio",
]


ENGINEERED_14 = DERIVED_13 + ["Speed_mech"]

COMBINED_20 = RAW_7 + DERIVED_13


REPRESENTATIONS = {
    "RAW_7": RAW_7,
    "ENGINEERED_14": ENGINEERED_14,
    "COMBINED_20": COMBINED_20,
}


def compute_physics_guided_features(
    df,
    epsilon=FEATURE_EPSILON_A,
):

    if epsilon <= 0:
        raise ValueError("epsilon must be positive.")

    missing = [
        c
        for c in CURRENT_COLUMNS
        if c not in df.columns
    ]

    if missing:
        raise ValueError(
            "Missing required current columns: "
            + str(missing)
        )

    s1 = df[
        CURRENT_COLUMNS[:3]
    ].to_numpy(
        dtype=np.float64,
        copy=False
    )

    s2 = df[
        CURRENT_COLUMNS[3:]
    ].to_numpy(
        dtype=np.float64,
        copy=False
    )

    if not np.isfinite(s1).all():
        raise ValueError(
            "Subsystem-1 RMS currents contain "
            "non-finite values."
        )

    if not np.isfinite(s2).all():
        raise ValueError(
            "Subsystem-2 RMS currents contain "
            "non-finite values."
        )

    if (s1 < 0).any() or (s2 < 0).any():
        raise ValueError(
            "RMS currents must be non-negative."
        )

    mean1 = s1.mean(axis=1)
    mean2 = s2.mean(axis=1)

    imbalance1 = (
        np.max(
            np.abs(
                s1 - mean1[:, None]
            ),
            axis=1
        )
        /
        np.maximum(
            mean1,
            epsilon
        )
    )

    imbalance2 = (
        np.max(
            np.abs(
                s2 - mean2[:, None]
            ),
            axis=1
        )
        /
        np.maximum(
            mean2,
            epsilon
        )
    )

    signed_diff = s1 - s2

    abs_diff = np.abs(
        signed_diff
    )

    log_ratio = np.log(
        (s1 + epsilon)
        /
        (s2 + epsilon)
    )

    matrix = np.column_stack([
        mean1,
        mean2,

        imbalance1,
        imbalance2,

        signed_diff[:, 0],
        signed_diff[:, 1],
        signed_diff[:, 2],

        abs_diff[:, 0],
        abs_diff[:, 1],
        abs_diff[:, 2],

        log_ratio[:, 0],
        log_ratio[:, 1],
        log_ratio[:, 2],
    ])

    if not np.isfinite(matrix).all():
        raise ValueError(
            "Derived features contain "
            "non-finite values."
        )

    return pd.DataFrame(
        matrix.astype(np.float32),
        columns=DERIVED_13,
        index=df.index,
    )


def build_feature_representation(
    df,
    representation,
):

    if representation not in REPRESENTATIONS:
        raise ValueError(
            "Unknown representation: "
            + str(representation)
        )

    missing = [
        c
        for c in RAW_7
        if c not in df.columns
    ]

    if missing:
        raise ValueError(
            "Missing frozen predictor columns: "
            + str(missing)
        )

    raw = df[
        RAW_7
    ].copy()

    for col in RAW_7:

        values = pd.to_numeric(
            raw[col],
            errors="raise"
        ).to_numpy(
            dtype=np.float64
        )

        if not np.isfinite(values).all():
            raise ValueError(
                f"{col} contains non-finite values."
            )

        raw[col] = raw[col].astype(
            np.float32
        )

    if representation == "RAW_7":
        return raw

    derived = (
        compute_physics_guided_features(
            df
        )
    )

    if representation == "ENGINEERED_14":

        out = derived.copy()

        out["Speed_mech"] = (
            raw["Speed_mech"]
        )

        return out[
            ENGINEERED_14
        ]

    out = pd.concat(
        [
            raw,
            derived,
        ],
        axis=1
    )

    return out[
        COMBINED_20
    ]
