#GHOSTRAVEN

**A tamper-evident lab that measures how far a defined attacker can recover a secret.**

Built by **Team KARMIN** for **Async 2026** · Track: **Cybersecurity & Defense**

**Live demo:** https://charming-gaufre-637b90.netlify.app

---

## The Problem

In *Harvest Now, Decrypt Later* attacks, adversaries steal encrypted data today and wait for cheaper compute, a leaked key, or a quantum breakthrough to unlock it. Nobody has a controlled way to measure how close that "later" already is.

Vague claims like "quantum is 10–20 years away" give organizations no basis for deciding what to protect first. Decisions get made on belief, not evidence.

**Who is affected:** anyone holding data that must stay secret for years, including defence and aerospace, satellite links, medical records, financial agreements, government files, IP, and AI-training data.

## The Solution

GHOSTRAVEN is a controlled lab that **measures, not guesses**, attacker recovery capability.

We plant a synthetic secret, seal a tamper-evident "witness" of it, then let a strictly defined attacker (fixed hardware, time, energy, and method) try to recover it across a ladder of increasingly hard challenges.

**Output:** a signed **Observed Recovery Frontier**, the highest challenge rung a specific attacker profile could break, used to prioritize what to re-encrypt first.

## How It Works

1. Plant secret
2. Derive session-bound witness (HKDF-SHA-256)
3. Seal commitment
4. Clear the secret
5. Run the controlled attack
6. Verify against the witness
7. Check controls (positive, negative, leakage canary)
8. Sign the report

**Witness escrow / split control:** generation, sealing, attacking, and verifying are handled by separate parties.

## Key Features

- **Challenge ladder:** four rungs (R1–R4), from 28-bit to 62-bit
- **Session-bound witnesses** using HKDF-SHA-256
- **Commit-then-clear** evidence flow
- **Positive, negative, and leakage-canary controls**
- **Hash-chained, Merkle-sealed audit trail**
- **Adversary envelope testing:** same asset, multiple attacker budgets, like a flight envelope in aerospace
- **Frontier drift detection:** rerun the same benchmark over time to see whether recovery gets easier as tools improve
- **Cross-domain long-life risk mode:** risk scored by secrecy duration, not just current attack cost
- **Evidence-linked migration tickets:** one per task, with a proof bundle attached

## What Makes It Different

We don't claim to break AES-256 or predict quantum computers. We build the missing tool. Every recovery claim is cryptographically verifiable, not just asserted, so a result reads as:

> "Under this attacker, this budget, this challenge family, recovery stopped here."

## Tech Stack

| Component | Technology |
|---|---|
| Challenge generator | Python |
| Witness derivation | HKDF-SHA-256 |
| Recovery workers | GPU |
| Evidence logger | Hash chain + Merkle tree |

## MVP Scope

- Four-rung challenge ladder (28-bit to 62-bit)
- One defined attacker profile (single GPU, fixed hours and energy budget)
- Full commit → clear → attack → verify flow with controls

## Success Metrics

- Correct frontier detection across all four ladder rungs
- Zero false leakage-canary hits
- Fully verifiable hash-chained audit trail

**Demo outcome:** a live run that closes with a signed statement such as *"Attacker Profile A recovered up to R2, not R3, within Budget Y."*

## Team KARMIN

- **Team lead:** Abhinava N.
- **Members (USN):** 1MS25IM003, 1MS25AS002, 1MS25IS106, 1MS25IS133

---

*Built for Async 2026, Cybersecurity & Defense track.*
