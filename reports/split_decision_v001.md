# P02 — SPLIT-001 Decision v001

## 1. Status

Specification:

P02-SPLIT-001 v001

Status:

FROZEN

## 2. Primary Development Protocol

Development uses simulated data only.

Grouping unit:

Load × SpeedRef

All FaultCodes belonging to the same operating condition
must remain in the same partition.

SIM_TRAIN conditions:

296

SIM_VALIDATION conditions:

72

SIM_TRAIN rows:

1,111,135

SIM_VALIDATION rows:

270,459

Actual validation row fraction:

0.1958

Exact Load × SpeedRef overlap:

0

## 3. Candidate A Rejection

Candidate A used FaultCode × Load × SpeedRef groups.

It produced exact Load × SpeedRef overlap for:

357 / 368 operating conditions.

Candidate A is therefore rejected as the primary
development split because nearly every validation operating
condition is represented in training under another
FaultCode.

## 4. Measured External Test

All 331,078 measured rows are assigned to:

MEASURED_EXTERNAL_TEST

Measured operating conditions:

321

Measured conditions outside simulation support:

0

Measured data are prohibited from:

- scaler fitting
- feature fitting
- model fitting
- hyperparameter tuning
- threshold tuning
- early stopping
- primary model selection

The measured population is reserved for final zero-shot
sim-to-real evaluation.

## 5. Auxiliary Unseen-Speed Protocol

The following SpeedRef values are completely held out:

[1000, 1100, 1300, 1900, 2200, 2500, 2800, 4200, 4400]

This protocol is auxiliary.

It is not used for primary model selection.

Model architecture, preprocessing choices, feature choices,
and hyperparameters must be locked using the primary
development protocol before the unseen-speed stress
protocol is evaluated.

## 6. Scaling Consequence

Any fitted scaler must be fitted using SIM_TRAIN only.

The same train-fitted transformation is applied unchanged
to:

- SIM_VALIDATION
- MEASURED_EXTERNAL_TEST

No measured-domain scaler is permitted for the core
experiment.

## 7. Leakage Controls

Prohibited:

- random row splitting
- FaultCode × Load × SpeedRef random grouping
- moving measured rows into development
- fitting transformations before the split
- using measured performance for primary model selection

## 8. Still Unfrozen

- exact physics-guided feature formulas
- final engineered feature set
- fitted scaler values
- evaluation metrics
- class-imbalance treatment
- conventional baseline model families
- deep-learning hypothesis and architecture

## 9. Next Step

FEAT-001 — freeze physics-guided feature specification.
