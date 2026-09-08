# P02 — Zero-Shot Sim-to-Real Baseline Result v001

## 1. Evaluation

TEST-001

Evaluation type:

Zero-shot simulation-to-measured transfer.

Measured rows:

331,078

Engineering groups:

6,086

The exact BASE-003 selected fitted models were used.

No model refit was performed before TEST-001.

No measured-domain scaling, threshold tuning, feature
selection or hyperparameter tuning was performed.

## 2. Simulation Development Results

Primary SIM_VALIDATION hierarchical Macro F1:

1.0000

Unseen-SpeedRef auxiliary hierarchical Macro F1:

1.0000

The conventional baseline therefore solved both frozen
simulation-domain evaluations.

## 3. Measured Stage A — Healthy versus Fault

Selected model:

HistGradientBoostingClassifier + ENGINEERED_14

Macro F1:

0.4865

Balanced Accuracy:

0.5000

MCC:

0.0000

AUROC:

0.5099

95% Macro-F1 CI:

[0.4865, 0.4865]

Observed failure mode:

All 6,086 measured engineering groups were predicted as
FAULT.

Measured population:

- 320 HEALTHY groups
- 5,766 FAULT groups

Healthy recall:

0.0000

The Stage-A detector therefore has essentially no useful
zero-shot measured-domain discrimination.

## 4. Measured Stage B — Fault-Group Localization

Selected model:

HistGradientBoostingClassifier + RAW_7

Macro F1:

0.9861

Balanced Accuracy:

0.9861

95% Macro-F1 CI:

[0.9789, 0.9922]

Fault-group localization transfers very strongly from
simulation to measurement.

## 5. Hierarchical Four-Class System

Macro F1:

0.7198

Balanced Accuracy:

0.7396

MCC:

0.9068

95% Macro-F1 CI:

[0.7145, 0.7243]

The relatively high MCC is driven by excellent prediction
of the much larger fault population and should not obscure
the complete failure of HEALTHY detection.

Macro F1 and per-class metrics are therefore required for
interpretation.

## 6. Primary Sim-to-Real Finding

The observed sim-to-real domain gap is strongly
task-dependent.

Fault-group localization transfers almost perfectly.

Healthy-versus-fault detection does not.

The measured-domain degradation is therefore concentrated
at the first diagnostic gate rather than throughout the
hierarchical classifier.

## 7. Baseline Integrity

TEST-001 does not alter the selected baseline.

No baseline tuning will be performed using TEST-001.

The conventional zero-shot result is permanently retained
as the reference baseline.

## 8. Next Step

A post-TEST-001 modeling decision gate is required before
additional measured-domain diagnostics or DL/domain
adaptation work.

Any subsequent method must be defined as a new
hypothesis-driven experiment and must not rewrite the
TEST-001 baseline result.
