# P02 — Compact Measured-Data and Domain-Gap Audit v001

## 1. Audit

P02-MEASURED-COMPACT-DOMAIN-GAP-001

Status: COMPLETE

## 2. Selected Measured Dataset

ZIP member:

`Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/measured/pkl/tmp_preprocessed_100_100_5000_none_test_all_faults_measured.pickle`

Persistent copy:

`/content/drive/MyDrive/NVH_DeepLearning/02_PMSM_SimToReal_Diagnosis/data/raw/measured/compact_audit_sample/tmp_preprocessed_100_100_5000_none_test_all_faults_measured.pickle`

Rows:

331,078

Columns:

11

## 3. Common Simulated / Measured Columns

- Currents_Sub1[1].rms
- Currents_Sub1[2].rms
- Currents_Sub1[3].rms
- Currents_Sub2[1].rms
- Currents_Sub2[2].rms
- Currents_Sub2[3].rms
- Speed_mech
- FaultCode
- Load
- Window
- SpeedRef

## 4. Candidate Common Primary Predictors

- Currents_Sub1[1].rms
- Currents_Sub1[2].rms
- Currents_Sub1[3].rms
- Currents_Sub2[1].rms
- Currents_Sub2[2].rms
- Currents_Sub2[3].rms
- Speed_mech

Current RMS channels common to both domains:

6

Mechanical speed common to both domains:

True

## 5. FaultCode Coverage

Simulated FaultCodes:

[0, 11, 12, 13, 14, 15, 16, 21, 22, 23, 24, 25, 26, 31, 32, 33, 34, 35, 36]

Measured FaultCodes:

[0.0, 11.0, 12.0, 13.0, 14.0, 15.0, 16.0, 21.0, 22.0, 23.0, 24.0, 25.0, 26.0, 31.0, 32.0, 33.0, 34.0, 35.0, 36.0]

## 6. Operating-Point Coverage

Simulated unique operating points:

6992

Measured unique operating points:

6086

Common operating points:

6086

## 7. Physics-Guided Feature Families

The following RMS-based physics-guided feature families
are feasible in both domains:

- subsystem_1_phase_rms_imbalance
- subsystem_2_phase_rms_imbalance
- cross_subsystem_phase_1_difference
- cross_subsystem_phase_1_ratio
- cross_subsystem_phase_2_difference
- cross_subsystem_phase_2_ratio
- cross_subsystem_phase_3_difference
- cross_subsystem_phase_3_ratio

Features requiring instantaneous phase information,
including true Clarke/Park transformations, symmetrical
components, phase-angle relationships, harmonics, and
electrical-order spectra, remain unavailable from the
compact RMS populations.

## 8. Sim-to-Real Domain Gap

A descriptive feature-by-feature comparison has been
persisted at:

`/content/drive/MyDrive/NVH_DeepLearning/02_PMSM_SimToReal_Diagnosis/results/tables/p02_01_4m/sim_to_real_global_domain_gap_v001.csv`

These statistics are exploratory only.

They are NOT:

- frozen normalization parameters
- model metrics
- data-selection thresholds
- acceptance criteria

## 9. Modeling Status

Common predictor space:

UNFROZEN

Target:

UNFROZEN

Physics-guided feature definitions:

UNFROZEN

Preprocessing:

UNFROZEN

Split:

UNFROZEN

Metrics:

UNFROZEN

Models:

UNFROZEN

Training:

NOT STARTED

## 10. Next Step

P02-01.5 — freeze the common simulated/measured
signal universe and initial diagnostic target.
