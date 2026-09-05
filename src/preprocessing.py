"""
P02 preprocessing implementation.

Specification:
    P02-PREP-001 v001

Important:
    - compact RMS rows are tabular samples
    - source row order is NOT interpreted as time
    - no scaler is fitted here
    - no row is silently removed
    - no engineered physics feature is created here
"""

import numpy as np
import pandas as pd


BASE_PREDICTORS = [
    "Currents_Sub1[1].rms",
    "Currents_Sub1[2].rms",
    "Currents_Sub1[3].rms",
    "Currents_Sub2[1].rms",
    "Currents_Sub2[2].rms",
    "Currents_Sub2[3].rms",
    "Speed_mech",
]

EXPECTED_SOURCE_COLUMNS = (
    BASE_PREDICTORS
    +
    [
        "FaultCode",
        "Load",
        "Window",
        "SpeedRef",
    ]
)

VALID_FAULT_CODES = (
    [0]
    +
    list(range(11, 17))
    +
    list(range(21, 27))
    +
    list(range(31, 37))
)

VALID_LOADS = [
    0, 5, 10, 15,
    20, 25, 30, 35,
]


def _require_integer_valued(series, name):
    values = pd.to_numeric(
        series,
        errors="raise"
    ).to_numpy(dtype=np.float64)

    if not np.all(np.isfinite(values)):
        raise ValueError(
            f"{name} contains non-finite values."
        )

    if not np.allclose(
        values,
        np.round(values)
    ):
        raise ValueError(
            f"{name} is not integer-valued."
        )


def decode_fault_code(code):
    code = int(code)

    if code == 0:
        return (
            "HEALTHY",
            "HEALTHY",
            0,
            0,
        )

    group = code // 10
    severity = code % 10

    if group not in (1, 2, 3):
        raise ValueError(
            f"Invalid fault group: {code}"
        )

    if severity not in (1, 2, 3, 4, 5, 6):
        raise ValueError(
            f"Invalid severity: {code}"
        )

    return (
        "FAULT",
        f"FAULT_GROUP_{group}",
        group,
        severity,
    )


def prepare_compact_frame(
    df,
    source_domain,
):
    """
    Canonicalize one compact P02 source frame.

    Parameters
    ----------
    df
        Public compact RMS dataframe.

    source_domain
        'simulated' or 'measured'.

    Returns
    -------
    pandas.DataFrame

    Notes
    -----
    source_row_ordinal is traceability metadata only.
    It MUST NOT be interpreted as time.
    """

    if source_domain not in {
        "simulated",
        "measured",
    }:
        raise ValueError(
            "source_domain must be simulated or measured."
        )

    if set(df.columns) != set(
        EXPECTED_SOURCE_COLUMNS
    ):
        raise ValueError(
            "Unexpected source schema."
        )

    if df[
        EXPECTED_SOURCE_COLUMNS
    ].isna().any().any():
        raise ValueError(
            "Missing values detected."
        )

    out = df[
        EXPECTED_SOURCE_COLUMNS
    ].copy()

    # --------------------------------------------------------
    # Base predictors
    # --------------------------------------------------------

    for col in BASE_PREDICTORS:

        values = pd.to_numeric(
            out[col],
            errors="raise"
        ).to_numpy(
            dtype=np.float64
        )

        if not np.all(
            np.isfinite(values)
        ):
            raise ValueError(
                f"{col} contains non-finite values."
            )

        out[col] = out[col].astype(
            np.float32
        )

    # --------------------------------------------------------
    # Integer-valued source metadata
    # --------------------------------------------------------

    for col in [
        "FaultCode",
        "Load",
        "SpeedRef",
        "Window",
    ]:

        _require_integer_valued(
            out[col],
            col,
        )

        out[col] = (
            out[col]
            .astype(np.int16)
        )

    # --------------------------------------------------------
    # Allowed values
    # --------------------------------------------------------

    observed_faults = sorted(
        out["FaultCode"]
        .unique()
        .tolist()
    )

    invalid_faults = sorted(
        set(observed_faults)
        -
        set(VALID_FAULT_CODES)
    )

    if invalid_faults:
        raise ValueError(
            "Unexpected FaultCode value(s): "
            + str(invalid_faults)
        )

    observed_loads = sorted(
        out["Load"]
        .unique()
        .tolist()
    )

    invalid_loads = sorted(
        set(observed_loads)
        -
        set(VALID_LOADS)
    )

    if invalid_loads:
        raise ValueError(
            "Unexpected Load value(s): "
            + str(invalid_loads)
        )

    if not (
        out["Speed_mech"] > 0
    ).all():
        raise ValueError(
            "Speed_mech must be positive."
        )

    if not (
        out["SpeedRef"] > 0
    ).all():
        raise ValueError(
            "SpeedRef must be positive."
        )

    if not (
        out["Window"] > 0
    ).all():
        raise ValueError(
            "Window must be positive."
        )

    # --------------------------------------------------------
    # Deterministic target decoding
    # --------------------------------------------------------

    decoded = [
        decode_fault_code(x)
        for x in out[
            "FaultCode"
        ].tolist()
    ]

    out[
        "binary_target"
    ] = [
        x[0]
        for x in decoded
    ]

    out[
        "location_target"
    ] = [
        x[1]
        for x in decoded
    ]

    out[
        "fault_group"
    ] = np.asarray(
        [
            x[2]
            for x in decoded
        ],
        dtype=np.int8
    )

    out[
        "severity_index"
    ] = np.asarray(
        [
            x[3]
            for x in decoded
        ],
        dtype=np.int8
    )

    # --------------------------------------------------------
    # Traceability metadata
    # --------------------------------------------------------

    out[
        "source_domain"
    ] = source_domain

    out[
        "source_row_ordinal"
    ] = np.arange(
        len(out),
        dtype=np.int64
    )

    # Condition grouping key.
    #
    # This does NOT freeze SPLIT-001.
    # It simply preserves a conservative grouping candidate.
    out[
        "condition_group_id"
    ] = (
        source_domain
        +
        "__FC"
        +
        out[
            "FaultCode"
        ].astype(str)
        +
        "__L"
        +
        out[
            "Load"
        ].astype(str)
        +
        "__SR"
        +
        out[
            "SpeedRef"
        ].astype(str)
    )

    return out
