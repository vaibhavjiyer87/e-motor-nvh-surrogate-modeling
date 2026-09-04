# P02 — Raw Simulated-Data Availability Audit v001

## 1. Audit Identity

P02-SIM-RAW-AVAILABILITY-001

Status:

COMPLETE

## 2. Purpose

Determine whether the public diagnosis archive exposes
raw simulated scenarios individually, so that P02 can
use richer time-series data without downloading or
generating an unnecessarily large simulation population.

## 3. Archive Summary

Total ZIP members:

149

Raw/intermediate simulated members:

3

Approximate uncompressed raw/intermediate volume:

31.33 GB

Raw members below 1 GB:

0

Raw members at or above 1 GB:

3

## 4. Raw / Intermediate Simulated Members

- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/simulated_test/dtw_test_v5.pickle` — 2879.07 MB uncompressed
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/simulated_test/model_v5/tmp_simulated_all_faults_v5.pickle` — 10645.75 MB uncompressed
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/data/simulated_training/tmp_training_all_faults_v5.pickle` — 18554.69 MB uncompressed

## 5. Individual Scenario Assessment

Scenario-like simulated data members detected:

6

Small individually addressable scenario-like members:

4

Assessment:

**RAW_DATA_APPEAR_BUNDLED_IN_LARGE_OBJECTS**

## 6. Compact Preprocessed Training Data

Preprocessed simulated training objects:

4

The previously audited unscaled object contains:

- six current RMS features
- mechanical speed
- FaultCode
- Load
- Window
- SpeedRef

## 7. Public Code / Preprocessing Support

Python or notebook files:

18

Potentially relevant code members:

18

- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/app_generator_data.py` — data | diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/app_model_validation.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/app_sbd.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/diagnosis/__init__.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/diagnosis/diagnose.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/generator/generator_data.py` — data | diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/generator/learn_classifier_model.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/generator/postprocess_data.py` — data | diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/interface/api_fmu_docker/__init__.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/interface/api_fmu_docker/api_lib.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/modules/__init__.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/modules/load_config.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/modules/module.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/modules/module_plot.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/modules/read_measured_data.py` — data | diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/simulation/__init__.py` — diagnosis | simulation
- `Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/simulation/simulation.py` — diagnosis | simulation
- `__MACOSX/Simulation-Based-Diagnosis_The Dual Three-Phase E-Motor_Experiment/simulation-based-diagnosis/._app_sbd.py` — diagnosis | simulation

## 8. Provisional Data-Path Recommendation

**USE_COMPACT_PREPROCESSED_DATA_UNLESS_CODE_AUDIT_REVEALS_SELECTIVE_EXTRACTION_ROUTE**

This is not yet a frozen modeling decision.

## 9. Physics-Guided Feature Watch

Candidate physically motivated features remain:

- phase RMS
- three-phase RMS imbalance
- cross-subsystem imbalance
- symmetrical components
- Clarke transformation
- Park / dq quantities when common data permit
- electrical-order-normalized current harmonics

No feature has been frozen.

## 10. Important Status

No full archive downloaded.

No raw multi-GB simulated object downloaded.

No simulations generated.

No predictor space frozen.

No target frozen.

No preprocessing frozen.

No model training started.

## 11. Next Step

P02-01.5 — freeze the common simulated/measured signal
universe and initial diagnostic target based on all
audited evidence.
