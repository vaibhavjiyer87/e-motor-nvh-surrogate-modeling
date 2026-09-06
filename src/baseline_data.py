
"""
P02 BASE-002 baseline-ready data loader.

Specification:
    P02-BASE-DATA-001 v001

This module does not train models.
"""

from pathlib import Path

import joblib
import numpy as np
import yaml


def load_baseline_data_spec(
    project_drive
):
    project_drive = Path(
        project_drive
    )

    path = (
        project_drive /
        "configs/baseline_data_v001.yaml"
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as f:
        return yaml.safe_load(f)


def load_combined_matrix(
    project_drive,
    mmap_mode="r",
):
    project_drive = Path(
        project_drive
    )

    spec = load_baseline_data_spec(
        project_drive
    )

    path = (
        project_drive /
        spec[
            "canonical_matrix"
        ]["path"]
    )

    return np.load(
        path,
        mmap_mode=mmap_mode,
        allow_pickle=False,
    )


def load_row_indices(
    project_drive,
    key,
):
    project_drive = Path(
        project_drive
    )

    spec = load_baseline_data_spec(
        project_drive
    )

    path = (
        project_drive /
        spec[
            "row_index_artifacts"
        ][key]
    )

    return np.load(
        path,
        allow_pickle=False,
    )


def load_training_weights(
    project_drive,
    stage,
):
    project_drive = Path(
        project_drive
    )

    spec = load_baseline_data_spec(
        project_drive
    )

    key = (
        "stage_a_train"
        if stage == "STAGE_A"
        else
        "stage_b_train"
    )

    path = (
        project_drive /
        spec[
            "weight_artifacts"
        ][key]
    )

    return np.load(
        path,
        allow_pickle=False,
    )


def load_scaler(
    project_drive,
    representation,
):
    project_drive = Path(
        project_drive
    )

    spec = load_baseline_data_spec(
        project_drive
    )

    path = (
        project_drive /
        spec[
            "scalers"
        ][representation]
    )

    return joblib.load(
        path
    )


def representation_column_indices(
    project_drive,
    representation,
):
    spec = load_baseline_data_spec(
        project_drive
    )

    return list(
        spec[
            "representation_indices"
        ][representation]
    )
