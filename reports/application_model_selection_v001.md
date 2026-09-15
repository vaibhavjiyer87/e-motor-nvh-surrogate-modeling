# P02 — Final Application Model Selection

## 1. Decision

Model exploration is complete.

The P02 application will use a hierarchical hybrid model:

### Stage A

MLP + ENGINEERED_14

Best source-model epoch:

3

Measured calibration threshold:

0.99945039

### Stage B

HistGradientBoostingClassifier + RAW_7

## 2. Why this architecture was selected

Stage A showed perfect simulation validation but severe
sim-to-real probability-scale shift.

The source-only MLP achieved measured AUROC 0.9348,
demonstrating useful cross-domain ranking despite failure of
the original 0.5 decision threshold.

Measured calibration recovered approximately 0.90 recall
for both HEALTHY and FAULT on held-out operating conditions.

Stage B transferred extremely well without modification,
achieving held-out Macro F1 0.9844.

A CNN was not selected because the frozen model-ready input
is tabular RMS data without reliable temporal ordering or a
natural convolutional representation.

Further model-family exploration was therefore not
considered justified.

## 3. Held-Out Application Evaluation

Stage A:

- Macro F1: 0.7246
- Balanced Accuracy: 0.9023
- HEALTHY Recall: 0.8984
- FAULT Recall: 0.9062

Stage B:

- Macro F1: 0.9844
- Balanced Accuracy: 0.9844

Hierarchical system:

- Macro F1: 0.8360
- Balanced Accuracy: 0.9043
- MCC: 0.8754

## 4. Qualification

APP-001 formal deployment acceptance:

FAIL

Reason:

Stage-A Macro F1 was below the frozen acceptance minimum of
0.80.

The model is nevertheless retained as an engineering-demo
model because it provides meaningful held-out performance
and clearly exposes the limitations of sim-to-real transfer.

## 5. Next Phase

No further model search is planned.

P02 proceeds to:

- inference contract
- model packaging
- standalone application
- model-card / About This Model interface
- end-to-end validation
