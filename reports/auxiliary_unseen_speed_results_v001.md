# P02 — AUX-001 Unseen-SpeedRef Robustness v001

## 1. Purpose

AUX-001 evaluates the already-selected conventional
baseline architecture against entire simulated SpeedRef
values excluded from auxiliary training.

This protocol is a robustness test.

It is not a second model-selection stage.

## 2. Frozen Architecture

Stage A:

HistGradientBoostingClassifier + ENGINEERED_14

Stage B:

HistGradientBoostingClassifier + RAW_7

No architecture, representation, hyperparameter or
threshold changes were allowed.

## 3. Held-Out SpeedRefs

The following SpeedRefs were completely excluded from
AUX_TRAIN:

- 1000
- 1100
- 1300
- 1900
- 2200
- 2500
- 2800
- 4200
- 4400

The selected recipes were retrained fresh using the
remaining simulated SpeedRefs.

## 4. Stage-A Result

Macro F1:

1.0000

Balanced Accuracy:

1.0000

MCC:

1.0000

95% Macro-F1 confidence interval:

[1.0000, 1.0000]

## 5. Stage-B Result

Macro F1:

1.0000

Balanced Accuracy:

1.0000

95% Macro-F1 confidence interval:

[1.0000, 1.0000]

## 6. Hierarchical Four-Class Result

Engineering groups:

1,368

Macro F1:

1.0000

Balanced Accuracy:

1.0000

MCC:

1.0000

95% Macro-F1 confidence interval:

[1.0000, 1.0000]

## 7. Interpretation

No performance degradation was observed when complete
SpeedRef values were withheld from auxiliary training.

The selected conventional baseline therefore appears robust
to this particular simulated-domain operating-speed shift.

This does not establish sim-to-real performance.

## 8. Model-Development Decision

The primary architecture remains unchanged.

No additional simulation-side baseline tuning will be
performed.

## 9. Protected Measured Evaluation

MEASURED_EXTERNAL_TEST has not been used.

No measured statistics, labels or predictions influenced:

- preprocessing
- feature selection
- model selection
- hyperparameters
- thresholds
- auxiliary robustness conclusions

## 10. Next Step

TEST-001 — perform the first one-shot zero-shot evaluation
of the locked baseline architecture on
MEASURED_EXTERNAL_TEST.
