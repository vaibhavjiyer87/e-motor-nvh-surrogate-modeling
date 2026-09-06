
"""
P02 baseline evaluation and weighting protocol.

Specification:
    P02-BASE-001 v001

No model training is performed by this module.
"""

import numpy as np
import pandas as pd

from sklearn.metrics import (
    balanced_accuracy_score,
    confusion_matrix,
    f1_score,
    matthews_corrcoef,
    precision_recall_fscore_support,
    roc_auc_score,
)


GROUP_COLUMNS = [
    "FaultCode",
    "Load",
    "SpeedRef",
]

CONDITION_COLUMNS = [
    "Load",
    "SpeedRef",
]


def make_group_class_balanced_sample_weights(
    metadata,
    class_col,
    group_cols=GROUP_COLUMNS,
):
    """
    Equalize total influence of each fault-condition group,
    then balance aggregate influence across classes.

    Raw row weight:

        (1 / rows_in_group)
        *
        (N_groups_total / (K * N_groups_in_class))

    Final weights are normalized to mean 1.
    """

    required = list(group_cols) + [class_col]

    missing = [
        c
        for c in required
        if c not in metadata.columns
    ]

    if missing:
        raise ValueError(
            "Missing weighting columns: "
            + str(missing)
        )

    meta = metadata[
        required
    ].reset_index(drop=True).copy()

    if meta.isna().any().any():
        raise ValueError(
            "Weighting metadata contain missing values."
        )

    group_class_counts = (
        meta
        .groupby(
            list(group_cols),
            observed=True,
        )[class_col]
        .nunique()
    )

    if (
        group_class_counts > 1
    ).any():

        raise ValueError(
            "A weighting group contains multiple classes."
        )

    unique_groups = (
        meta
        .drop_duplicates(
            subset=list(group_cols)
        )
    )

    class_group_counts = (
        unique_groups[
            class_col
        ]
        .value_counts()
    )

    n_groups_total = len(
        unique_groups
    )

    n_classes = len(
        class_group_counts
    )

    class_factor = {
        cls:
            n_groups_total
            /
            (
                n_classes
                *
                int(group_count)
            )

        for cls, group_count
        in class_group_counts.items()
    }

    group_size = (
        meta
        .groupby(
            list(group_cols),
            observed=True,
        )[class_col]
        .transform("size")
        .astype(np.float64)
    )

    class_factor_rows = (
        meta[
            class_col
        ]
        .map(
            class_factor
        )
        .astype(np.float64)
    )

    weights = (
        (1.0 / group_size)
        *
        class_factor_rows
    ).to_numpy()

    if not np.isfinite(weights).all():
        raise ValueError(
            "Non-finite sample weights."
        )

    if (weights <= 0).any():
        raise ValueError(
            "Sample weights must be positive."
        )

    weights = (
        weights
        /
        weights.mean()
    )

    return weights.astype(
        np.float64
    )


def aggregate_group_probabilities(
    metadata,
    probabilities,
    classes,
    true_label_col,
    group_cols=GROUP_COLUMNS,
):
    """
    Average row-level class probabilities within each
    FaultCode x Load x SpeedRef group, then predict argmax.
    """

    classes = list(classes)

    probs = np.asarray(
        probabilities,
        dtype=np.float64
    )

    if probs.ndim != 2:
        raise ValueError(
            "probabilities must be 2-D."
        )

    if probs.shape[1] != len(classes):
        raise ValueError(
            "Probability column count does not match classes."
        )

    if len(metadata) != probs.shape[0]:
        raise ValueError(
            "metadata and probabilities have different rows."
        )

    if not np.isfinite(probs).all():
        raise ValueError(
            "Probabilities contain non-finite values."
        )

    required = (
        list(group_cols)
        +
        [true_label_col]
    )

    missing = [
        c
        for c in required
        if c not in metadata.columns
    ]

    if missing:
        raise ValueError(
            "Missing aggregation columns: "
            + str(missing)
        )

    work = (
        metadata[
            required
        ]
        .reset_index(drop=True)
        .copy()
    )

    probability_columns = []

    for j, cls in enumerate(classes):

        col = (
            "prob_"
            +
            str(cls)
        )

        probability_columns.append(
            col
        )

        work[col] = probs[:, j]

    group_label_counts = (
        work
        .groupby(
            list(group_cols),
            observed=True,
        )[true_label_col]
        .nunique()
    )

    if (
        group_label_counts > 1
    ).any():

        raise ValueError(
            "A fault-condition group contains "
            "multiple true labels."
        )

    aggregation = {
        true_label_col:
            "first",
    }

    for col in probability_columns:
        aggregation[col] = "mean"

    grouped = (
        work
        .groupby(
            list(group_cols),
            observed=True,
            as_index=False,
            sort=True,
        )
        .agg(
            aggregation
        )
    )

    row_counts = (
        work
        .groupby(
            list(group_cols),
            observed=True,
            as_index=False,
            sort=True,
        )
        .size()
        .rename(
            columns={
                "size":
                    "rows_in_group"
            }
        )
    )

    grouped = grouped.merge(
        row_counts,
        on=list(group_cols),
        how="left",
        validate="one_to_one",
    )

    matrix = grouped[
        probability_columns
    ].to_numpy(
        dtype=np.float64
    )

    class_array = np.asarray(
        classes,
        dtype=object
    )

    grouped[
        "predicted_label"
    ] = class_array[
        np.argmax(
            matrix,
            axis=1
        )
    ]

    return grouped


def compute_group_classification_metrics(
    y_true,
    y_pred,
    labels,
    positive_probability=None,
    positive_label=None,
):
    """
    Return scalar, per-class and confusion-matrix metrics.
    """

    y_true = np.asarray(
        y_true,
        dtype=object
    )

    y_pred = np.asarray(
        y_pred,
        dtype=object
    )

    labels = list(labels)

    scalar = {
        "macro_f1":
            float(
                f1_score(
                    y_true,
                    y_pred,
                    labels=labels,
                    average="macro",
                    zero_division=0,
                )
            ),

        "balanced_accuracy":
            float(
                balanced_accuracy_score(
                    y_true,
                    y_pred,
                )
            ),

        "mcc":
            float(
                matthews_corrcoef(
                    y_true,
                    y_pred,
                )
            ),
    }

    if (
        positive_probability is not None
        and
        positive_label is not None
    ):

        score = np.asarray(
            positive_probability,
            dtype=np.float64
        )

        binary_truth = (
            y_true
            ==
            positive_label
        ).astype(int)

        if len(
            np.unique(
                binary_truth
            )
        ) == 2:

            scalar[
                "auroc"
            ] = float(
                roc_auc_score(
                    binary_truth,
                    score,
                )
            )

        else:

            scalar[
                "auroc"
            ] = np.nan

    precision, recall, f1, support = (
        precision_recall_fscore_support(
            y_true,
            y_pred,
            labels=labels,
            zero_division=0,
        )
    )

    per_class = pd.DataFrame({
        "label":
            labels,

        "precision":
            precision,

        "recall":
            recall,

        "f1":
            f1,

        "support":
            support,
    })

    cm = confusion_matrix(
        y_true,
        y_pred,
        labels=labels,
    )

    confusion = pd.DataFrame(
        cm,
        index=[
            f"true_{x}"
            for x in labels
        ],
        columns=[
            f"pred_{x}"
            for x in labels
        ],
    )

    return (
        scalar,
        per_class,
        confusion,
    )


def true_system_label_from_faultcode(
    fault_code
):
    """
    Convert frozen FaultCode to the four-class
    hierarchical system target.
    """

    code = int(
        fault_code
    )

    if code == 0:
        return "HEALTHY"

    group = (
        code // 10
    )

    if group not in [1, 2, 3]:
        raise ValueError(
            "Unexpected FaultCode: "
            + str(code)
        )

    return (
        "FAULT_GROUP_"
        +
        str(group)
    )


def compose_hierarchical_group_predictions(
    stage_a_groups,
    stage_b_groups,
    stage_a_pred_col="predicted_label",
    stage_b_pred_col="predicted_label",
    group_cols=GROUP_COLUMNS,
):
    """
    Combine Stage-A healthy/fault predictions with Stage-B
    location predictions.

    Stage-B probabilities/predictions should be generated
    for every evaluation group at inference time even though
    Stage-B model fitting/evaluation is fault-only.
    """

    a = stage_a_groups[
        list(group_cols)
        +
        [stage_a_pred_col]
    ].copy()

    a = a.rename(
        columns={
            stage_a_pred_col:
                "stage_a_prediction"
        }
    )

    b = stage_b_groups[
        list(group_cols)
        +
        [stage_b_pred_col]
    ].copy()

    b = b.rename(
        columns={
            stage_b_pred_col:
                "stage_b_prediction"
        }
    )

    merged = a.merge(
        b,
        on=list(group_cols),
        how="left",
        validate="one_to_one",
    )

    if (
        merged[
            "stage_b_prediction"
        ]
        .isna()
        .any()
    ):

        raise ValueError(
            "Stage-B prediction missing for "
            "one or more inference groups."
        )

    merged[
        "true_system_label"
    ] = merged[
        "FaultCode"
    ].map(
        true_system_label_from_faultcode
    )

    merged[
        "predicted_system_label"
    ] = np.where(
        merged[
            "stage_a_prediction"
        ]
        ==
        "HEALTHY",

        "HEALTHY",

        merged[
            "stage_b_prediction"
        ],
    )

    return merged


def bootstrap_macro_f1_by_condition(
    group_predictions,
    true_col,
    pred_col,
    labels,
    condition_cols=CONDITION_COLUMNS,
    n_bootstrap=1000,
    confidence_level=0.95,
    seed=20260906,
):
    """
    Percentile bootstrap CI for group-level Macro F1.

    Resampling unit:
        Load x SpeedRef operating condition.

    All fault-condition groups belonging to a sampled
    operating condition are kept together.
    """

    required = (
        list(condition_cols)
        +
        [true_col, pred_col]
    )

    missing = [
        c
        for c in required
        if c not in group_predictions.columns
    ]

    if missing:
        raise ValueError(
            "Missing bootstrap columns: "
            + str(missing)
        )

    work = (
        group_predictions[
            required
        ]
        .reset_index(drop=True)
        .copy()
    )

    condition_groups = [
        x
        for _, x
        in work.groupby(
            list(condition_cols),
            observed=True,
            sort=True,
        )
    ]

    n_conditions = len(
        condition_groups
    )

    if n_conditions < 2:
        raise ValueError(
            "At least two operating conditions "
            "are required for bootstrap."
        )

    rng = np.random.default_rng(
        seed
    )

    scores = np.empty(
        n_bootstrap,
        dtype=np.float64
    )

    for i in range(
        n_bootstrap
    ):

        sampled = rng.integers(
            0,
            n_conditions,
            size=n_conditions,
        )

        y_true_parts = []
        y_pred_parts = []

        for idx in sampled:

            part = condition_groups[
                int(idx)
            ]

            y_true_parts.append(
                part[
                    true_col
                ].to_numpy()
            )

            y_pred_parts.append(
                part[
                    pred_col
                ].to_numpy()
            )

        y_true = np.concatenate(
            y_true_parts
        )

        y_pred = np.concatenate(
            y_pred_parts
        )

        scores[i] = f1_score(
            y_true,
            y_pred,
            labels=list(labels),
            average="macro",
            zero_division=0,
        )

    alpha = (
        1.0
        -
        confidence_level
    )

    estimate = f1_score(
        work[
            true_col
        ],
        work[
            pred_col
        ],
        labels=list(labels),
        average="macro",
        zero_division=0,
    )

    return {
        "estimate":
            float(
                estimate
            ),

        "ci_low":
            float(
                np.quantile(
                    scores,
                    alpha / 2.0
                )
            ),

        "ci_high":
            float(
                np.quantile(
                    scores,
                    1.0 - alpha / 2.0
                )
            ),

        "confidence_level":
            float(
                confidence_level
            ),

        "bootstrap_replicates":
            int(
                n_bootstrap
            ),

        "seed":
            int(
                seed
            ),

        "resampling_unit":
            "Load_x_SpeedRef",
    }
