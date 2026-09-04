# Emotor_NVH_SurrogateModeling

<!-- P02_MANAGED_STATUS_V001 -->

# P02 — Sim-to-Real PMSM Fault Diagnosis

## Engineering Question

Can models trained primarily on publicly available
simulated dual three-phase PMSM diagnostic data detect
inter-turn short-circuit faults and identify the affected
fault-location group in real measured motor data?

## Current Frozen Checkpoint

Last completed:

**P02-01.5 — Common sim-to-real signal universe and
initial diagnostic target**

Next:

**PREP-001 — Freeze preprocessing specification**

## Frozen Base Predictors

1. `Currents_Sub1[1].rms`
2. `Currents_Sub1[2].rms`
3. `Currents_Sub1[3].rms`
4. `Currents_Sub2[1].rms`
5. `Currents_Sub2[2].rms`
6. `Currents_Sub2[3].rms`
7. `Speed_mech`

## Frozen Diagnostic Formulation

Stage A:

- `HEALTHY`
- `FAULT`

Stage B:

- `FAULT_GROUP_1`
- `FAULT_GROUP_2`
- `FAULT_GROUP_3`

Fault severity remains evaluation/stratification
metadata rather than the core target.

## Physics-Guided Feature Families

Approved for later `FEAT-001`:

- within-subsystem phase RMS imbalance
- subsystem mean RMS current
- corresponding-phase cross-subsystem differences
- corresponding-phase cross-subsystem ratios

## Data / Repository Boundary

GitHub stores:

- source code
- frozen specifications
- small registries
- reports
- compact result tables

Google Drive stores:

- raw/public datasets
- large intermediate datasets
- checkpoints
- large model artifacts
- persistent runtime state
