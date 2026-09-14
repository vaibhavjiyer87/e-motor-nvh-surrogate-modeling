# P02 — DL-001 Stage-A MLP Hypothesis v001

## 1. Purpose

DL-001 is the first neural-network experiment in P02.

It targets the specific weakness exposed by TEST-001:
zero-shot Stage-A HEALTHY-versus-FAULT transfer.

## 2. Controlled Comparison

The selected conventional Stage-A baseline uses:

HistGradientBoosting + ENGINEERED_14.

DL-001 intentionally keeps ENGINEERED_14 unchanged.

This isolates model-family effects before introducing
domain adaptation or representation changes.

## 3. Neural Model

Architecture:

14 -> 64 -> 32 -> 16 -> 2

Each hidden layer uses:

- Linear
- LayerNorm
- ReLU
- Dropout 0.10

Optimizer:

AdamW.

## 4. Development Protocol

Training:

SIM_TRAIN only.

Epoch selection and early stopping:

SIM_VALIDATION group-level Macro F1 only.

The same leakage-safe condition split used by the
conventional baseline is retained.

## 5. Measured Data Policy

Measured data are not used for:

- training
- early stopping
- hyperparameter tuning
- feature selection
- model selection

TEST-001 has already been observed.

Therefore any later measured result for DL-001 is explicitly
a post-test exploratory comparison and is not a pristine
external validation.

## 6. Decision Logic

DL-001 answers a narrow question:

Can a neural decision function improve on the tree-based
Stage-A model while all input features are held constant?

If not, more complex DL methods are not justified merely
because they are neural.

If the simulation result is competitive, a later experiment
may test explicit domain adaptation.
