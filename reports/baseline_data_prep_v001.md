# P02 — BASE-002 Baseline-Ready Data Preparation v001

## 1. Status

P02-BASE-DATA-001 v001

Status: FROZEN

No classifier training has started.

## 2. Data Domain

Only simulated data were loaded and materialized.

MEASURED_EXTERNAL_TEST remained sealed.

No measured feature matrix was generated.

## 3. Canonical Feature Matrix

A single COMBINED_20 float32 matrix was persisted.

Rows:

1,381,594

Columns:

20

RAW_7 and ENGINEERED_14 are deterministic column views of
this matrix rather than duplicate stored matrices.

## 4. Primary Development Rows

SIM_TRAIN:

1,111,135

SIM_VALIDATION:

270,459

## 5. Stage B

Stage-B training uses true-fault SIM_TRAIN rows only.

Rows:

1,052,667

Stage-B development validation uses true-fault
SIM_VALIDATION rows only.

Rows:

256,227

## 6. Sample Weights

Stage A:

group-equalized and class-balanced using SIM_TRAIN only.

Stage B:

group-equalized and class-balanced using fault-only
SIM_TRAIN data.

Both weight arrays are normalized to mean 1.

No oversampling or undersampling is used.

## 7. Standard Scaling

Three StandardScaler artifacts were fitted:

RAW_7
ENGINEERED_14
COMBINED_20

All scalers were fitted on SIM_TRAIN only.

Scaling is unweighted.

SIM_VALIDATION statistics were not used.

Measured statistics were not used.

## 8. Crash-Safe Experiment Registry

Fourteen BASE-001 experiment slots were created.

Each slot has a deterministic configuration fingerprint.

Initial state:

PENDING

The live registry is stored on persistent Google Drive.

Completed experiment records must never be overwritten by a
fresh session with matching fingerprints.

## 9. Next Step

BASE-003 — run conventional baseline experiments using
model-by-model crash-safe persistence.

The first classifier fit has not yet occurred.
