
"""
P02 conventional baseline estimator definitions.

Specification:
    P02-BASE-001 v001

This module defines estimators only.
Importing/building an estimator does NOT train it.
"""

from sklearn.dummy import DummyClassifier
from sklearn.ensemble import HistGradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler


BASELINE_SEED = 20260906


VALID_MODEL_FAMILIES = [
    "DUMMY_PRIOR",
    "LOGISTIC_REGRESSION",
    "HIST_GRADIENT_BOOSTING",
]


VALID_REPRESENTATIONS = [
    "RAW_7",
    "ENGINEERED_14",
    "COMBINED_20",
]


def build_baseline_estimator(
    model_family,
):
    """
    Construct one frozen BASE-001 estimator.

    No fitting is performed here.
    """

    if (
        model_family
        ==
        "DUMMY_PRIOR"
    ):

        return DummyClassifier(
            strategy="prior",
            random_state=BASELINE_SEED,
        )


    if (
        model_family
        ==
        "LOGISTIC_REGRESSION"
    ):

        return Pipeline([
            (
                "scaler",
                StandardScaler(),
            ),
            (
                "classifier",
                LogisticRegression(
                    C=1.0,
                    solver="lbfgs",
                    max_iter=1000,
                    random_state=BASELINE_SEED,
                ),
            ),
        ])


    if (
        model_family
        ==
        "HIST_GRADIENT_BOOSTING"
    ):

        return HistGradientBoostingClassifier(
            learning_rate=0.08,
            max_iter=250,
            max_leaf_nodes=31,
            l2_regularization=1.0,
            early_stopping=False,
            random_state=BASELINE_SEED,
        )


    raise ValueError(
        "Unknown model_family: "
        + str(model_family)
    )


def sample_weight_fit_parameter(
    model_family,
):
    """
    Return the correct sklearn fit keyword for sample weights.
    """

    if (
        model_family
        ==
        "LOGISTIC_REGRESSION"
    ):
        return "classifier__sample_weight"

    if model_family in [
        "DUMMY_PRIOR",
        "HIST_GRADIENT_BOOSTING",
    ]:
        return "sample_weight"

    raise ValueError(
        "Unknown model_family: "
        + str(model_family)
    )


def requires_scaling(
    model_family,
):
    return (
        model_family
        ==
        "LOGISTIC_REGRESSION"
    )
