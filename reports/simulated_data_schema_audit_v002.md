# P02 — Simulated Data Schema Audit v002

## 1. Audit

P02-SIM-SCHEMA-001R

Status: COMPLETE

## 2. Repair

The original v001 audit incorrectly selected:

`Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/simulated_training/tmp_preprocessed_100_100_5000_none_training_scaler_all_faults_v5.pickle`

That object was a scaler-related artifact and
deserialized as integer `0`.

It is not a simulated training dataset.

## 3. Corrected Training Object

`Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/simulated_training/tmp_preprocessed_100_100_5000_none_training_all_faults_v5.pickle`

Persistent path:

`/content/drive/MyDrive/NVH_DeepLearning/02_PMSM_SimToReal_Diagnosis/data/raw/simulated/schema_audit_sample/tmp_preprocessed_100_100_5000_none_training_all_faults_v5.pickle`

Size:

115.95 MB

CRC32:

b64780a8

SHA256:

af67d91322cca52d82e5e975997f0e6b7ae8b2dfe2f68c25e053c2c1df20bd08

Top-level Python type:

DataFrame

Schema entries:

12

## 4. Archive Status

Full ~16 GB archive downloaded:

NO

New simulation generation:

NO

## 5. Modeling Status

Predictors:

UNFROZEN

Target:

UNFROZEN

Windowing:

UNFROZEN

Representation:

UNFROZEN

Normalization:

UNFROZEN

Split:

UNFROZEN

Metrics:

UNFROZEN

Models:

UNFROZEN

## 6. Next Step

P02-01.5 — compare this corrected simulated-data
schema with the measured-data schema and decide the
common sim-to-real signal universe and initial target.
