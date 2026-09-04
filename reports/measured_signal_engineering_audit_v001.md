# P02 — Measured Signal Engineering Audit v001

## 1. Audit Identity

Audit ID:

P02-MEASURED-SIGNAL-CONTENT-001

Status:

COMPLETE

## 2. Source Run

File:

`spd10-5000rpm_flt0z_20NM.mat`

Condition:

- Healthy
- 0 shorted turns
- 20 Nm load

Measured duration:

41.500 s

Verified sample rate:

10000.000 Hz

Maximum measured speed:

4399.71 rpm

## 3. Available Dynamic Signal Families

The raw file contains:

- six phase currents across two three-phase subsystems
- four dq current channels
- measured and requested speed
- electrical angle sine/cosine channels
- four dq voltage/control channels

P02 predictor channels remain UNFROZEN.

## 4. Exploratory Quasi-Steady Audit Interval

An exploratory interval was identified solely for
engineering visualization.

Start:

20.877400 s

End:

21.596400 s

Mean speed:

575.47 rpm

Speed range:

23.77 rpm

This selection logic is NOT PREP-001 and must not be
treated as a frozen modeling rule.

## 5. Phase-Current Audit

Six synchronized phase-current channels were inspected.

Artifacts include:

- time histories
- RMS / peak statistics
- subsystem three-phase balance
- corresponding-phase subsystem comparison
- Welch spectral estimates

These descriptors are diagnostic observations only and
are not frozen ML predictors.

## 6. dq-Current Audit

The four dq-current channels were summarized for
engineering context.

No decision has been made to include or exclude dq
signals from the eventual model.

## 7. Important Modeling Implication

The measured signal population contains rich
multichannel temporal structure together with substantial
speed variation.

The eventual sim-to-real predictor space should therefore
be chosen only after verifying which equivalent signals
exist in the public simulated training population.

## 8. Frozen Status After P02-01.3

Predictor channels:

UNFROZEN

Prediction target:

UNFROZEN

Window length:

UNFROZEN

Overlap:

UNFROZEN

Spectral representation:

UNFROZEN

Normalization:

UNFROZEN

Split:

UNFROZEN

Metrics:

UNFROZEN

Model families:

UNFROZEN

## 9. Next Step

P02-01.4 — Simulated-data schema audit.

The purpose of P02-01.4 is to identify the common
measured/simulated signal universe before any modeling
specification is created.
