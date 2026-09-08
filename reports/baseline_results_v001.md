# P02 — Conventional Baseline Results v001

## 1. Status

BASE-003 COMPLETE.

Primary conventional baseline architecture is locked using
SIM_VALIDATION only.

Neither protected evaluation protocol was used for model
selection.

## 2. Stage A — Healthy vs Fault

Selected model:

HistGradientBoostingClassifier

Selected representation:

ENGINEERED_14

SIM_VALIDATION group-level results:

- Macro F1: 1.0000
- Balanced Accuracy: 1.0000
- MCC: 1.0000
- 95% Macro-F1 CI: [1.0000, 1.0000]

The physics-guided representation materially improved
Stage-A performance relative to RAW_7.

The COMBINED_20 representation achieved the same ceiling,
so ENGINEERED_14 was selected by the frozen
fewer-predictors tie-break rule.

## 3. Stage B — Fault-Group Localization

Selected model:

HistGradientBoostingClassifier

Selected representation:

RAW_7

SIM_VALIDATION group-level results:

- Macro F1: 1.0000
- Balanced Accuracy: 1.0000
- 95% Macro-F1 CI: [1.0000, 1.0000]

All HistGradientBoosting representations achieved the same
perfect score.

RAW_7 was therefore selected by the frozen
fewer-predictors tie-break rule.

## 4. Hierarchical System

Four classes:

- HEALTHY
- FAULT_GROUP_1
- FAULT_GROUP_2
- FAULT_GROUP_3

SIM_VALIDATION engineering groups:

1,368

Results:

- Macro F1: 1.0000
- Balanced Accuracy: 1.0000
- MCC: 1.0000
- 95% Macro-F1 CI: [1.0000, 1.0000]

## 5. Engineering Interpretation

The simulation-domain results indicate two different feature
needs across the diagnostic hierarchy.

Stage A benefits strongly from physics-guided current-level,
imbalance, cross-subsystem difference and ratio features.

Stage B already contains sufficient location information in
the raw RMS phase-current representation.

Using different representations for the two stages is
therefore intentional.

## 6. Model-Development Decision

No additional conventional-baseline hyperparameter tuning
will be performed at this stage.

The leakage-safe simulation-validation problem has already
reached the metric ceiling.

Further tuning would not provide a meaningful model-selection
signal and would increase overfitting risk.

## 7. Protected Evaluations

MEASURED_EXTERNAL_TEST:

NOT USED.

Auxiliary unseen-SpeedRef protocol:

NOT USED.

No sim-to-real performance claim is made from BASE-003.

## 8. Next Step

Evaluate the frozen selected architecture on the auxiliary
unseen-SpeedRef protocol.

This is a robustness test and must not change the selected
primary model architecture.

Only after that robustness evaluation should the protected
measured external test be opened.
