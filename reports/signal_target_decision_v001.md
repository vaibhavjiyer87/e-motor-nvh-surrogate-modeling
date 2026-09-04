# P02 — Common Signal Universe and Target Decision v001

## 1. Decision Identity

P02-SIGNAL-TARGET-001

Status: FROZEN

Frozen after:

P02-01.5

## 2. Core P02 Data Representation

P02 will use the existing compact public
speed-adaptive RMS datasets as its core simulated
and measured populations.

The bundled multi-GB raw simulated population is
not required for the core project.

## 3. Frozen Base Predictor Universe

1. Currents_Sub1[1].rms
2. Currents_Sub1[2].rms
3. Currents_Sub1[3].rms
4. Currents_Sub2[1].rms
5. Currents_Sub2[2].rms
6. Currents_Sub2[3].rms
7. Speed_mech

These seven variables exist with matching semantics
in both simulated and measured compact datasets.

## 4. Non-Predictor Columns

FaultCode:

Target source.

Load:

Operating-condition metadata used for grouping,
stratification, and robustness analysis.

SpeedRef:

Operating/control metadata used for grouping and
coverage analysis.

Window:

Preprocessing metadata. It is not treated as an
independent model predictor.

## 5. Frozen Diagnostic Target

The core diagnostic task is hierarchical.

### Stage A — Fault Detection

Classes:

- HEALTHY
- FAULT

### Stage B — Fault Location Group

Conditional on a detected fault:

- FAULT_GROUP_1
- FAULT_GROUP_2
- FAULT_GROUP_3

The compact FaultCode structure is:

- 0 = healthy
- 11–16 = fault group 1
- 21–26 = fault group 2
- 31–36 = fault group 3

Physical U/V/W names are intentionally not attached
to these groups until the exact public preprocessing
mapping is explicitly verified.

## 6. Fault Severity

The ones digit of FaultCode provides severity levels
1–6.

Severity is retained as:

- stratification metadata
- robustness metadata
- diagnostic difficulty metadata

Exact severity prediction is NOT a core P02 target.

## 7. Physics-Guided Feature Families

The following feature families are approved for
development in FEAT-001:

- within-subsystem phase RMS imbalance
- subsystem mean RMS current
- corresponding-phase cross-subsystem difference
- corresponding-phase cross-subsystem ratio

These exploit physical structure of the dual
three-phase machine.

## 8. Features Not Supported by Compact RMS Data

The core compact dataset cannot faithfully support:

- Clarke alpha-beta transforms
- Park dq transforms from instantaneous phase current
- symmetrical-component phasors
- phase-angle features
- current harmonic features
- electrical-order spectra

These require instantaneous waveform information.

## 9. Domain-Gap Policy

The measured and simulated compact tables have the
same schema.

Global current-RMS summary statistics are similar,
but the measured and simulated speed distributions
differ substantially.

This does NOT establish condition-wise domain
equivalence.

Any normalization parameters must therefore be fit
using training data only.

Operating speed and load must be explicitly considered
during split design and evaluation.

## 10. Still Unfrozen

- exact feature formulas
- final conventional feature set
- normalization
- train/validation/test split
- metrics
- model families
- DL architecture
- hyperparameters
- deployment format

## 11. Next Step

PREP-001 — freeze preprocessing specification.

After PREP-001:

SPLIT-001 — freeze leakage-safe experimental design
before any model training.
