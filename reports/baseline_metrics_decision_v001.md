# P02 — BASE-001 Baseline and Metrics Decision v001

## 1. Specification

P02-BASE-001 v001

Status: FROZEN

No model training has started.

## 2. Engineering Evaluation Unit

Primary evaluation is not performed per RMS row.

Predicted probabilities are averaged within each:

FaultCode × Load × SpeedRef

group.

One engineering prediction is then produced per group.

This prevents conditions containing more repeated RMS rows
from carrying disproportionate evaluation weight.

## 3. Stage A

Task:

HEALTHY vs FAULT

Primary selection metric:

Group-level Macro F1

Tie breakers:

1. Balanced Accuracy
2. MCC
3. Fewer predictors
4. Simpler model family
5. Lexical model ID

AUROC is diagnostic only.

## 4. Stage B

Task:

FAULT_GROUP_1 vs FAULT_GROUP_2 vs FAULT_GROUP_3

Training and selection are conditional on true fault cases.

Primary selection metric:

Group-level Macro F1

Tie breakers:

1. Balanced Accuracy
2. Fewer predictors
3. Simpler model family
4. Lexical model ID

## 5. Hierarchical System

Final diagnostic labels:

HEALTHY
FAULT_GROUP_1
FAULT_GROUP_2
FAULT_GROUP_3

Primary system-level reporting metric:

4-class group-level Macro F1

This metric does not override separately selected Stage-A
and Stage-B models.

## 6. Representations

RAW_7

ENGINEERED_14

COMBINED_20

## 7. Conventional Baselines

Sanity floor:

DummyClassifier(strategy="prior")

Linear baseline:

LogisticRegression

C = 1.0
solver = lbfgs
max_iter = 1000

StandardScaler is fitted on SIM_TRAIN only.

Strong nonlinear tabular baseline:

HistGradientBoostingClassifier

learning_rate = 0.08
max_iter = 250
max_leaf_nodes = 31
l2_regularization = 1.0
early_stopping = False

No first-pass hyperparameter search is allowed.

## 8. Class Imbalance

No oversampling.

No undersampling.

Each FaultCode × Load × SpeedRef group first receives equal
aggregate influence.

Row weight within group:

1 / rows_in_group

Class balancing factor:

N_groups_total / (K × N_groups_in_class)

Final training weights are normalized so their mean equals
1.

Weights are calculated from the active SIM_TRAIN training
population only.

## 9. Probability Decision Policy

Stage A:

argmax class probability
(binary equivalent threshold = 0.5)

Stage B:

argmax class probability

No threshold tuning in BASE-001.

## 10. Bootstrap Reporting

95% percentile bootstrap confidence intervals.

Resampling unit:

Load × SpeedRef

Replicates:

1000

Seed:

20260906

Bootstrap confidence intervals are for reporting only and
are not used for model selection.

## 11. Protected Evaluation Domains

MEASURED_EXTERNAL_TEST remains sealed until primary
simulation-domain model selection is locked.

The auxiliary unseen-SpeedRef protocol also remains sealed
until primary model selection is locked.

Neither may be used for:

- scaling
- feature selection
- threshold tuning
- hyperparameter tuning
- primary model selection

## 12. Crash-Safe Baseline Persistence

Each stage/model/representation fit is one recoverable
experiment.

Immediately after each successful fit:

- persist model artifact
- persist metrics
- persist group predictions
- persist configuration fingerprint
- update experiment registry

Completed experiments with matching fingerprints are skipped
after restart.

Writes use temporary files followed by atomic replacement
where practical.

## 13. Still Unfrozen

- fitted scaler parameters
- baseline experiment registry
- final selected Stage-A model
- final selected Stage-B model
- final external-test refit policy
- deep-learning hypothesis
- deep-learning architecture

## 14. Next Step

BASE-002 — prepare baseline-ready data, training weights,
fitted train-only scaling artifacts, and crash-safe
experiment registry before the first model fit.
