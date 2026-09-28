#  GHOSTRAVEN

### A Tamper-Evident Lab That Measures How Far a Defined Attacker Can Recover a Secret

**Team KARMIN | Cybersecurity & Defense | ASYNC 2026**

---

##   Overview

**GHOSTRAVEN** is a controlled cybersecurity laboratory that measures attacker recovery capability instead of simply assuming that a cryptographic system is secure.

The system creates a synthetic secret, generates a session-bound cryptographic witness, commits the evidence, clears the original secret, and then allows a strictly defined attacker to attempt recovery across increasingly difficult challenge levels.

The final output is an **Observed Recovery Frontier** — the highest challenge level successfully recovered by a specific attacker under a defined computational budget.

---

##  Problem

In a **Harvest Now, Decrypt Later** scenario, an attacker can:

```text
Encrypted Data
      ↓
Ciphertext Stolen Today
      ↓
Wait for Better Capabilities
      ↓
Attempt Decryption Later
```

Organizations therefore need a practical way to understand how close a defined attacker is to successful recovery.

This matters for long-life sensitive information including aerospace, satellite, medical, financial, government, legal and intellectual-property data.

---

##  Our Solution

GHOSTRAVEN replaces assumptions with a controlled experiment:

```text
Plant Secret
     ↓
Derive Witness
     ↓
Seal Commitment
     ↓
Clear Secret
     ↓
Run Attack
     ↓
Verify Recovery
     ↓
Check Controls
     ↓
Sign Report
```

The attacker is constrained by a defined:

* Hardware configuration
* Time budget
* Energy budget
* Attack method
* Challenge family

This makes the result reproducible and auditable.

---

##  Architecture

![GHOSTRAVEN Architecture](docs/images/architecture.png)

### Main Components

| Component           | Technology               |
| ------------------- | ------------------------ |
| Challenge Generator | Python                   |
| Witness Derivation  | HKDF-SHA-256             |
| Recovery Workers    | GPU                      |
| Verification        | Cryptographic witness    |
| Evidence            | Hash Chain + Merkle Tree |
| Final Output        | Signed Recovery Report   |

The MVP uses a four-rung challenge ladder from **28-bit to 62-bit**, one defined attacker profile, and the complete commit → clear → attack → verify pipeline.

---

##  Challenge Ladder

![Challenge Ladder](docs/images/challenge-ladder.png)

```text
R1 ── 28-bit       → Easy
 ↓
R2                 → Medium
 ↓
R3                 → Hard
 ↓
R4 ── 62-bit       → Hardest
```

The experiment determines where the attacker stops.

Example:

```text
R1 →  Recovered
R2 →  Recovered
R3 →  Not recovered
R4 →  Not recovered

Observed Recovery Frontier = R2
```

---

##  Evidence & Verification

GHOSTRAVEN uses a **session-bound HKDF-SHA-256 witness** and a commit-then-clear workflow.

The system also uses:

* Positive controls
* Negative controls
* Leakage canaries
* Hash-chained evidence
* Merkle-sealed evidence

These mechanisms ensure that a recovery claim is **verified rather than simply asserted**.

---

##  Observed Recovery Frontier

The main result of an experiment is a signed statement such as:

> **Attacker Profile A recovered up to R2, not R3, within Budget Y.**

The result can then be connected to an evidence bundle and used to prioritize systems for re-encryption.

![Recovery Frontier](docs/images/recovery-frontier.png)

---


##  Future Scope

* Multiple attacker profiles
* Distributed recovery workers
* Historical frontier tracking
* Frontier drift detection
* Automated migration tickets
* Evidence-linked re-encryption workflows

The project proposes rerunning standardized benchmarks over time to observe whether recovery becomes easier as tools and capabilities improve.

---

##  Team KARMIN

**Track:** Cybersecurity & Defense
**Event:** ASYNC 2026

**Team Lead:** Abhinava N.

---

