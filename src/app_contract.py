from __future__ import annotations

from dataclasses import dataclass
from typing import List

import numpy as np
import pandas as pd


APP_INPUT_COLUMNS = [
    "Currents_Sub1[1].rms",
    "Currents_Sub1[2].rms",
    "Currents_Sub1[3].rms",
    "Currents_Sub2[1].rms",
    "Currents_Sub2[2].rms",
    "Currents_Sub2[3].rms",
    "Speed_mech",
]


CURRENT_RMS_COLUMNS = [
    "Currents_Sub1[1].rms",
    "Currents_Sub1[2].rms",
    "Currents_Sub1[3].rms",
    "Currents_Sub2[1].rms",
    "Currents_Sub2[2].rms",
    "Currents_Sub2[3].rms",
]


@dataclass(frozen=True)
class InputValidationResult:
    dataframe: pd.DataFrame
    warnings: List[str]


def validate_app_input(
    dataframe: pd.DataFrame,
) -> InputValidationResult:

    if not isinstance(dataframe, pd.DataFrame):
        raise TypeError(
            "Application input must be a pandas DataFrame."
        )

    if len(dataframe) == 0:
        raise ValueError(
            "Input contains zero rows."
        )

    if dataframe.columns.duplicated().any():
        duplicates = (
            dataframe.columns[
                dataframe.columns.duplicated()
            ]
            .tolist()
        )

        raise ValueError(
            "Duplicate column names are not allowed: "
            f"{duplicates}"
        )

    missing = [
        column
        for column in APP_INPUT_COLUMNS
        if column not in dataframe.columns
    ]

    if missing:
        raise ValueError(
            "Missing required input columns: "
            f"{missing}"
        )

    warnings = []

    extra = [
        column
        for column in dataframe.columns
        if column not in APP_INPUT_COLUMNS
    ]

    if extra:
        warnings.append(
            "Extra columns were ignored: "
            + ", ".join(extra)
        )

    cleaned = (
        dataframe[
            APP_INPUT_COLUMNS
        ]
        .copy()
    )

    for column in APP_INPUT_COLUMNS:

        cleaned[column] = pd.to_numeric(
            cleaned[column],
            errors="raise",
        )

    values = cleaned.to_numpy(
        dtype=np.float64,
        copy=False,
    )

    if not np.isfinite(values).all():
        raise ValueError(
            "Input contains NaN or infinite values."
        )

    if (
        cleaned[
            CURRENT_RMS_COLUMNS
        ]
        .to_numpy()
        <
        0
    ).any():

        raise ValueError(
            "RMS current inputs cannot be negative."
        )

    if len(cleaned) == 1:
        warnings.append(
            "Single-row inference is technically supported, "
            "but model validation was performed using "
            "multi-row engineering groups."
        )

    return InputValidationResult(
        dataframe=cleaned,
        warnings=warnings,
    )
