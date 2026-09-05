# P02 — PREP-001 Preprocessing Decision v001

## 1. Specification

Specification ID:

P02-PREP-001

Version:

v001

Status:

FROZEN

## 2. Source Representation

The core P02 public datasets contain compact,
speed-adaptive RMS current observations.

The public source pickles remain read-only.

No raw-waveform reconstruction is performed.

## 3. Modeling Representation

Each compact RMS row is represented as a tabular
observation.

Row order is NOT interpreted as:

- time
- sequence position
- chronological order
- independent physical experiment identity

The compact datasets do not provide an explicit
time/sample/sequence index sufficient to justify that
interpretation.

Sequence modeling is therefore NOT enabled by PREP-001.

Repeated observations are preserved and grouping metadata
is carried forward to SPLIT-001.

## 4. Frozen Base Predictors

1. Currents_Sub1[1].rms
2. Currents_Sub1[2].rms
3. Currents_Sub1[3].rms
4. Currents_Sub2[1].rms
5. Currents_Sub2[2].rms
6. Currents_Sub2[3].rms
7. Speed_mech

## 5. Source Metadata

FaultCode:

Target source.

Load:

Operating-condition metadata.

SpeedRef:

Operating-condition metadata.

Window:

Speed-dependent preprocessing metadata.

None of Load, SpeedRef, or Window is added to the frozen
base predictor space.

## 6. Data Integrity Policy

PREP-001 uses fail-fast validation.

The pipeline does not silently:

- remove missing rows
- remove non-finite rows
- deduplicate observations
- clip outliers
- winsorize values
- repair invalid FaultCodes

Source-data inconsistencies require an explicit versioned
decision rather than silent modification.

## 7. Canonical Modeling Dtypes

Seven base predictors:

float32

FaultCode:

int16

Load:

int16

SpeedRef:

int16

Window:

int16

Derived group/severity integer metadata:

int8 where appropriate.

## 8. Target Decoding

Stage A:

HEALTHY / FAULT

Stage B:

FAULT_GROUP_1 /
FAULT_GROUP_2 /
FAULT_GROUP_3

Severity levels 1–6 remain evaluation and stratification
metadata.

Physical U/V/W names remain unresolved.

## 9. Scaling Policy

Tree-based models:

No feature scaling required.

Scale-sensitive models, including linear models, SVMs,
neural networks, and autoencoders:

StandardScaler.

IMPORTANT:

Scaler parameters must be fitted using TRAINING DATA ONLY
after SPLIT-001 is frozen.

The same train-fitted transformation must be applied to
validation and test data.

Independent simulated-domain and measured-domain scalers
are prohibited for the core sim-to-real experiment.

No scaler is fitted during PREP-001.

## 10. Physics-Guided Features

Approved physics-guided feature families will be
calculated from unscaled RMS values.

Exact formulas remain deferred to FEAT-001.

Approved families:

- subsystem phase RMS imbalance
- subsystem mean RMS current
- cross-subsystem corresponding-phase difference
- cross-subsystem corresponding-phase ratio

## 11. Speed / Domain Policy

Speed_mech remains a base predictor.

No automatic restriction to common simulated/measured
speed support is applied during preprocessing.

Operating-range split and evaluation policy is deferred
to SPLIT-001.

## 12. Class-Balance Policy

No oversampling, undersampling, SMOTE, or class weighting
occurs during preprocessing.

Any class-balance treatment must occur only after
SPLIT-001 and only using training data.

## 13. Traceability

Modeling tables will preserve:

- source domain
- original source-row ordinal
- condition grouping metadata

source-row ordinal is traceability metadata only and
MUST NOT be treated as time.

## 14. Still Unfrozen

- train / validation / test split
- exact physics-guided feature formulas
- final engineered feature set
- fitted scaler parameters
- evaluation metrics
- conventional model families
- deep-learning hypothesis
- hyperparameters

## 15. Next Step

SPLIT-001 — freeze leakage-safe experimental design.
