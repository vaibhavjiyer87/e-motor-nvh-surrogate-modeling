# About This Model

## What this application does

This application demonstrates fault detection and
fault-group identification for a dual three-phase PMSM
using RMS current features and motor speed.

## Model architecture

The application uses two models.

### Stage A — Fault detection

Model:

MLP neural network

Inputs:

ENGINEERED_14 physics-guided RMS features

Output:

HEALTHY or FAULT

Measured-domain decision threshold:

0.99945039

### Stage B — Fault-group identification

Model:

HistGradientBoostingClassifier

Inputs:

RAW_7

Output:

FAULT_GROUP_1, FAULT_GROUP_2, or FAULT_GROUP_3

## What the model does well

- Fault-group localization transfers very strongly from
  simulated to measured data.

- Stage-B held-out measured Macro F1 is 0.9844.

- The complete hierarchical system achieved held-out
  Balanced Accuracy of 0.9043.

- The Stage-A MLP retained strong ranking information across
  the simulation-to-measurement domain gap.

## Important limitations

### 1. Stage-A classification did not meet the frozen
deployment criterion

Held-out Stage-A Macro F1:

0.7246

The predefined deployment requirement was:

0.80

Therefore this model is not claimed to be production
qualified.

### 2. Measured calibration is required

A threshold of 0.5 worked in simulation but did not transfer
to measured data.

The final engineering-demo model uses a measured-domain
threshold of:

0.99945039

This large shift is evidence of a substantial
simulation-to-measurement probability calibration gap.

### 3. Dataset scope is limited

The model was developed and evaluated using the public PMSM
dataset used in this project.

Performance on other motors, sensors, controllers,
operating ranges, acquisition systems, or fault mechanisms
has not been established.

### 4. Fault groups are intentionally generic

The application reports:

- FAULT_GROUP_1
- FAULT_GROUP_2
- FAULT_GROUP_3

Physical U/V/W phase labels are not asserted because the
required source mapping was not independently verified.

### 5. Severity is not predicted

The model identifies fault presence and fault group.

It does not provide a validated estimate of shorted-turn
severity.

## Intended use

Engineering demonstration, education, portfolio work, and
diagnostic-support prototyping.

## Not intended for

Safety-critical or production decisions without additional
independent validation.
