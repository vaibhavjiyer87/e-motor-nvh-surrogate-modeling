# P02 — FEAT-001 Feature Decision v001

## 1. Specification

P02-FEAT-001 v001

Status: FROZEN

## 2. Frozen Feature Families

13 physics-guided derived features:

- subsystem mean RMS
- subsystem phase-RMS imbalance
- corresponding-phase signed difference
- corresponding-phase absolute difference
- corresponding-phase natural-log ratio

## 3. Frozen Representations

RAW_7

ENGINEERED_14

COMBINED_20

## 4. Derivation Policy

All physics-guided features are calculated from unscaled RMS
current values.

Speed_mech is retained as the operating-context predictor.

## 5. Numerical Safeguard

epsilon = 1e-06 A

epsilon is fixed and is not fitted from data.

## 6. Scaling Policy

Any required scaler is fitted using SIM_TRAIN only.

SIM_VALIDATION and MEASURED_EXTERNAL_TEST use exactly the
same train-fitted transformation.

## 7. Measured-Test Protection

Measured distributions were not used for feature selection.

Measured target associations were not used for feature
selection.

Measured performance was not used for pruning.

## 8. Redundancy Audit

SIM_TRAIN pairs with |Pearson r| >= 0.995:

1

All 13 derived features remain frozen for the baseline
representation comparison.

## 9. Feature Pruning

No supervised feature pruning is allowed before the first
conventional baseline comparison.

## 10. Implementation Repair

FEAT-001B1-R corrected an ordering-only implementation issue
in the feature-definition table.

The mathematical feature specification was unchanged.

The corrected table is explicitly ordered according to the
canonical DERIVED_13 feature list.

## 11. Next Stage

BASE-001 — freeze evaluation metrics, class-imbalance
treatment, baseline model families, model-selection policy,
random seeds, and persistence rules before training.
