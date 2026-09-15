# P02 — APP-001 Deployment Calibration Protocol

## Purpose

P02 has stopped general model exploration.

The application candidate is a hierarchical hybrid:

- Stage A: MLP + ENGINEERED_14
- Stage B: HistGradientBoosting + RAW_7

The Stage-A neural model achieved perfect simulation
validation and measured AUROC 0.9348, but its simulation
decision threshold did not transfer to the measured domain.

APP-001 therefore tests the simplest engineering remedy:
measured-domain decision-threshold calibration.

## Calibration Design

Measured Load × SpeedRef operating conditions are divided
into:

- APP_CALIBRATION: 60%
- APP_EVALUATION: 40%

All FaultCode groups belonging to an operating condition
remain together.

No row-random split is allowed.

## Allowed Use

APP_CALIBRATION labels may be used only to select the
Stage-A group-level decision threshold.

The trained MLP weights are frozen.

The Stage-B HistGradientBoosting model is frozen.

## Held-Out Evaluation

APP_EVALUATION is not used for threshold selection.

The frozen threshold is evaluated once against the
held-out conditions.

## Acceptance Criteria

Stage-A APP_EVALUATION must achieve:

- Macro F1 >= 0.80
- Balanced Accuracy >= 0.80
- HEALTHY recall >= 0.70
- FAULT recall >= 0.90

If these conditions pass, the hybrid architecture becomes
eligible for the standalone application.

If they fail, APP_EVALUATION will not be used to retune the
threshold.

## CNN Decision

A CNN is not currently justified because the frozen
model-ready data are tabular RMS features without reliable
temporal ordering or a natural convolutional representation.
