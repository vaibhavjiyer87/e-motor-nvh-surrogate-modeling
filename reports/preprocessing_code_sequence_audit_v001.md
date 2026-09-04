# P02 — Preprocessing-Code and RMS-Sequence Audit v001

## 1. Audit

P02-PREPROCESS-CODE-SEQUENCE-001

Status: COMPLETE

## 2. Compact Simulated Dataset

Rows:

1,381,594

Columns:

11

Available predictors / metadata:

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

## 3. Operating / Sequence Metadata

Unique FaultCode values:

19

Unique Load values:

8

Unique SpeedRef values:

46

Unique Window values:

46

Data-structure sequence assessment:

**PARTIAL_SEQUENCE_STRUCTURE_AVAILABLE**

## 4. Public Preprocessing Code

Python scripts audited:

17

Approximate total source size:

0.492 MB

Code mentions RMS:

True

Code mentions Window:

True

Code mentions SpeedRef:

True

## 5. Combined Assessment

**DATA_SUPPORT_SEQUENCE_MODELING_BUT_CODE_EVIDENCE_PARTIAL**

## 6. Raw-Data Decision

The raw simulated time histories remain bundled in
multi-GB objects.

P02 will not download those objects merely to obtain a
more complex neural-network input.

The compact public dataset remains the preferred core
population unless the final modeling decision identifies
a specific reason that requires raw signals.

## 7. Physics-Guided Feature Implications

The six phase-current RMS channels support several
physically motivated derived descriptors without
requiring raw waveforms:

- within-subsystem phase RMS imbalance
- corresponding-phase cross-subsystem differences
- corresponding-phase cross-subsystem ratios
- subsystem average current level
- maximum/minimum phase-current spread

Features requiring instantaneous phase information,
including true Clarke/Park transforms and symmetrical
components, cannot be reconstructed faithfully from
RMS magnitudes alone.

## 8. Next Step

P02-01.5 — freeze the common simulated/measured signal
universe and initial diagnostic target.
