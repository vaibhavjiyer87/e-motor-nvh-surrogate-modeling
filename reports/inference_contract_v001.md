# P02 — Application Inference Contract

## 1. Purpose

This document defines the exact input and output boundary
for the standalone P02 engineering-demo application.

The application does not train or adapt models at runtime.

## 2. Input

One inference request represents one operating capture.

The preferred input format is CSV.

Each row must contain seven values:

1. Currents_Sub1[1].rms
2. Currents_Sub1[2].rms
3. Currents_Sub1[3].rms
4. Currents_Sub2[1].rms
5. Currents_Sub2[2].rms
6. Currents_Sub2[3].rms
7. Speed_mech

Load, SpeedRef and FaultCode are not model inputs.

Labels are not required.

The application must not require users to construct the
ENGINEERED_14 features themselves.

## 3. Input semantics

A batch should represent one operating capture.

Rows from unrelated operating conditions should not be
combined into a single inference request.

The validated inference behavior uses multiple RMS rows and
aggregates model outputs across the batch.

Single-row inference may execute technically, but it was not
the primary validation granularity and must produce a user
warning.

## 4. Stage A

The application internally derives ENGINEERED_14 from the
six RMS current channels and Speed_mech.

The frozen SIM_TRAIN StandardScaler is then applied.

The frozen Stage-A MLP produces a FAULT score for each row.

The application averages those row scores.

The frozen decision threshold is:

0.99945039

If the mean score is below the threshold, the result is:

HEALTHY

Otherwise:

FAULT

The Stage-A score must be displayed as a "Fault score".

It must not be represented as a calibrated probability or
model confidence.

## 5. Stage B

Stage B runs only when Stage A reports FAULT.

The frozen HistGradientBoosting model uses RAW_7 directly.

Row-level class probabilities are averaged over the input
batch.

The highest mean probability determines:

- FAULT_GROUP_1
- FAULT_GROUP_2
- FAULT_GROUP_3

The application must not rename these groups to physical
U/V/W phases unless that mapping is independently verified.

## 6. Output

The main result must include:

- diagnostic status
- fault group when applicable
- Stage-A fault score
- Stage-A threshold
- number of rows processed
- model version
- qualification status
- warnings

## 7. Qualification

The application model is:

ENGINEERING DEMONSTRATION — ACCEPTED WITH LIMITATIONS

It is not production qualified.

## 8. Transparency

The primary results screen must provide an:

About This Model

button or equivalent control.

That view will display the frozen model card, including
strengths, limitations, dataset scope and validation results.
