# P02 — Measured Signal Schema Audit v001

## 1. Audit ID

P02-MEASURED-SIGNAL-SCHEMA-001

Status: COMPLETE

## 2. Source File

`spd10-5000rpm_flt0z_20NM.mat`

Condition:

- shorted turns: 0
- fault phase: HEALTHY
- load torque: 20 Nm

Nominal published sampling rate:

10,000 Hz

MAT-file reader:

MATLAB pre-v7.3 / scipy.loadmat

## 3. Purpose

This audit inspects one raw measured PMSM file
to establish the actual signal schema before any
preprocessing or ML formulation is frozen.

## 4. Candidate Long Numeric Signals

- `Currents_SubSys1_A` — shape=(415001,), dtype=float32, range=[-108.53277587890625, 107.67236328125]
- `Currents_SubSys1_B` — shape=(415001,), dtype=float32, range=[-111.24948120117188, 113.58566284179688]
- `Currents_SubSys1_C` — shape=(415001,), dtype=float32, range=[-112.03573608398438, 111.436767578125]
- `Currents_SubSys1_d` — shape=(415001,), dtype=float32, range=[-21.918874740600586, 17.36275291442871]
- `Currents_SubSys1_q` — shape=(415001,), dtype=float32, range=[43.440269470214844, 114.34687805175781]
- `Currents_SubSys2_A` — shape=(415001,), dtype=float32, range=[-112.36642456054688, 112.24166870117188]
- `Currents_SubSys2_B` — shape=(415001,), dtype=float32, range=[-106.08660888671875, 109.664306640625]
- `Currents_SubSys2_C` — shape=(415001,), dtype=float32, range=[-109.81640625, 111.38507080078125]
- `Currents_SubSys2_d` — shape=(415001,), dtype=float32, range=[-25.1220645904541, 18.457210540771484]
- `Currents_SubSys2_q` — shape=(415001,), dtype=float32, range=[38.58119583129883, 114.24757385253906]
- `SinCos_Electrical_Cos` — shape=(415001,), dtype=float32, range=[-0.9999997615814209, 0.9999998807907104]
- `SinCos_Electrical_Sin` — shape=(415001,), dtype=float32, range=[-0.9999998807907104, 0.9999999403953552]
- `Speed_rad_el` — shape=(415001,), dtype=float32, range=[-3.8251256942749023, 4607.3671875]
- `Speed_requred_rad_el` — shape=(415001,), dtype=float32, range=[0.0, 4631.40869140625]
- `Speed_requred_rpm` — shape=(415001,), dtype=float32, range=[0.0, 4422.66943359375]
- `Speed_rpm` — shape=(415001,), dtype=float32, range=[-3.6527259349823, 4399.7119140625]
- `Time` — shape=(415001,), dtype=float64, range=[0.0, 41.5]
- `Voltage_SubSys1_d` — shape=(415001,), dtype=float32, range=[-45.711849212646484, 1.5876437425613403]
- `Voltage_SubSys1_q` — shape=(415001,), dtype=float32, range=[3.263866424560547, 58.53559112548828]
- `Voltage_SubSys2_d` — shape=(415001,), dtype=float32, range=[-45.838680267333984, 2.025766372680664]
- `Voltage_SubSys2_q` — shape=(415001,), dtype=float32, range=[2.815747022628784, 59.05335998535156]

## 5. Important Restrictions

This audit does NOT:

- select predictor channels
- select the final diagnostic target
- define window duration
- define overlap
- define normalization
- define train/validation/test populations
- train any model

## 6. Statistical Rule

The original measured run remains the physical
grouping unit.

Future windows generated from this file must
inherit the grouping of this source run.

## 7. Next Decision

The next audit step will interpret the discovered
signals and determine which channels warrant
engineering visualization before PREP-001 is
created.
