<div align="center">

# 👻⚛️ GHOSTRAVEN

### Evidence-Guided Post-Quantum Migration Intelligence

**You can't protect what you haven't measured. GHOSTRAVEN measures it.**

[![Async 2026](https://img.shields.io/badge/ASYNC-2026-black?style=for-the-badge)](https://charming-gaufre-637b90.netlify.app)
[![Track](https://img.shields.io/badge/Track-Cybersecurity%20%26%20Defense-red?style=for-the-badge)](#)
[![Status](https://img.shields.io/badge/Status-Alpha-orange?style=for-the-badge)](#-maturity--benchmarks)
[![License](https://img.shields.io/badge/License-TBD-lightgrey?style=for-the-badge)](#-governance--license)

[![Build](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square)](#)
[![Coverage](https://img.shields.io/badge/coverage-pending-yellow?style=flat-square)](#)
[![Code Quality](https://img.shields.io/badge/code%20quality-A-brightgreen?style=flat-square)](#)
[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=flat-square&logo=python)](#)
[![Crypto](https://img.shields.io/badge/Witness-HKDF--SHA--256-9cf?style=flat-square)](#)
[![Evidence](https://img.shields.io/badge/Audit-Hash%20Chain%20%2B%20Merkle-purple?style=flat-square)](#)

**[🚀 Live Demo](https://charming-gaufre-637b90.netlify.app) · [📐 Architecture](#2️⃣-architecture--system-design) · [⚡ Quick Start](#3️⃣-installation--configuration) · [🧠 Why We Win](#-why-this-should-win) · [🛡️ Security](#-security-reporting)**

<br/>

<img src="images/page.png" alt="GHOSTRAVEN dashboard" width="880"/>

<sub>GHOSTRAVEN's migration-prioritization dashboard — live demo above</sub>

</div>

<br/>

> ```diff
> + Harvest Now, Decrypt Later is already happening — today, right now.
> - "Quantum is 10-20 years away" is not a migration plan. It's a guess.
> + GHOSTRAVEN replaces that guess with signed, reproducible, court-grade evidence.
> ```

---

## 📑 Table of Contents

1. [Context & Overview](#1️⃣-context--overview)
2. [Architecture & System Design](#2️⃣-architecture--system-design)
3. [Installation & Configuration](#3️⃣-installation--configuration)
4. [Developer Experience & Quality Control](#4️⃣-developer-experience--quality-control)
5. [Reliability, Performance & Security](#5️⃣-reliability-performance--security)
6. [Governance & License](#6️⃣-governance--license)
7. [Why This Should Win](#-why-this-should-win)
8. [Judge FAQ](#-judge-faq)
9. [Team](#-team)

---

## 1️⃣ Context & Overview

### 🎯 Elevator Pitch

**GHOSTRAVEN is an evidence-guided post-quantum security platform that tells organizations exactly *which systems must migrate first* to quantum-safe cryptography — and proves the recommendation with signed, reproducible, tamper-evident evidence instead of vendor marketing or guesswork.**

It is built for the systems where getting this wrong is catastrophic and irreversible: **aerospace, defense, satellite operations, healthcare, banking, telecom, and critical infrastructure** — anywhere data must stay confidential for years or decades.

### 🧩 The Problem We Solve

**Harvest Now, Decrypt Later (HNDL):** adversaries steal encrypted data *today*, store it, and simply wait — for cheaper compute, a leaked key, or a cryptographically relevant quantum computer — to decrypt it *later*.

```
┌─────────────┐    ┌─────────────┐    ┌──────────────────────┐    ┌─────────────────┐
│ Encrypted   │ →  │ Harvested   │ →  │ Wait                 │ →  │ Decrypted later │
│ today       │    │ (stolen now)│    │ cheaper compute ·    │    │ how close is    │
│             │    │             │    │ leaked key · quantum │    │ "later"?        │
└─────────────┘    └─────────────┘    └──────────────────────┘    └─────────────────┘
```

Every security leader already knows HNDL is real. **What nobody has had is a defensible, evidence-based way to answer the only question that actually matters:**

> *"Of everything we hold, what has to migrate first — and how do we prove that priority list to an auditor, a board, or a regulator?"*

That's the gap GHOSTRAVEN closes.

### ⚠️ What GHOSTRAVEN Never Does

> 🔒 **Hard boundary, by design:** GHOSTRAVEN never attacks real customer files, production databases, private keys, passwords, AES-256, RSA, ECC, or any PQC algorithm. Every experiment runs against **synthetic, harmless, lab-generated assets** that mimic the operational shape of a real system without containing any real data. This isn't a limitation — it's what makes the evidence usable in an audit instead of a liability.

### 🌟 Core Capabilities

| Capability | What it does | Why it matters |
|---|---|---|
| 🪪 **Crypto Asset Passport** | Per-asset profile: algorithm, protocol, data sensitivity, secrecy lifetime, criticality, owner, dependencies, exposure, upgrade difficulty, PQC readiness | Turns "we have a lot of old crypto somewhere" into a structured, queryable inventory |
| 📊 **Urgency Scoring Engine** | Ranks assets by quantum exposure, long-term confidentiality need, mission impact, dependency blast radius, and migration difficulty | Converts the inventory into a prioritized, defensible migration order — not a flat checklist |
| 🧪 **Synthetic Recovery Lab** | Generates harmless synthetic files, databases, telemetry, and challenge secrets that mirror real system shape with zero real data | Lets you *measure* attacker capability safely, instead of theorizing about it |
| 🎯 **Observed Recovery Frontier** | Runs a fixed, disclosed attacker profile (hardware, time, memory, energy, method) against the synthetic ladder | Produces a signed, specific claim: *this* attacker, with *this* budget, got *this* far — nothing vaguer |
| ✅ **Evidence Validation** | Positive controls, negative controls, leakage canaries, config checks, budget limits — every run labeled `Verified`, `Inconclusive`, `Contaminated`, or `Invalid` | No result ships without proof the experiment itself was sound |
| ⛓️ **Tamper-Evident Chain** | Hash chains, Merkle roots, config hashes, digital signatures, signed receipts | Makes silent report modification *mathematically detectable*, not just policy-forbidden |
| 🤖 **AI Analyst (advisory only)** | Explains anomalies, missing evidence, and migration options in plain language | Speeds up human review — but **never** decides what's true |
| 🍯 **Decoy Archives & Honeytokens** | Harmless fake assets that silently alert security when an intruder maps systems, probes synthetic archives, or attempts exfiltration | Free, passive early-warning layer with zero risk to real data |
| 🛡️ **Cryptographic Exoskeleton** | A modern gateway wrapped around legacy systems that can't yet adopt PQC directly: restricts routes, blocks direct exposure, flags bypass/downgrade attempts, opens hybrid/PQC tunnels | Protects what you can't replace overnight — without pretending it's been fixed |
| 📒 **Residual-Risk Ledger** | Tracks remaining endpoint, local-network, and gateway risk after the Exoskeleton is deployed | Keeps the "temporary fix" honest about what risk is still outstanding |
| 🎫 **Evidence-Linked Migration Tickets** | Owner, recommended action, protection status, retest schedule, full-upgrade deadline, retirement clock | Guarantees the Exoskeleton is a *bridge*, with an expiry date — never a forgotten workaround |

### 🧠 The One-Sentence Difference

> Other tools tell you **encryption exists**. GHOSTRAVEN tells you, with signed proof, **how much that encryption is actually worth, against whom, for how long — and what to fix first.**

### 🎥 Demo

**Live walkthrough:** [charming-gaufre-637b90.netlify.app](https://charming-gaufre-637b90.netlify.app)

<div align="center">
<img src="images/frontier.png" alt="GHOSTRAVEN Observed Recovery Frontier" width="880"/>
<br/><sub>Observed Recovery Frontier across the synthetic challenge ladder — the attacker opens easy rungs, stalls on hard ones</sub>
</div>

---

## 2️⃣ Architecture & System Design

### 🏗️ System Architecture

<div align="center">
<img src="images/architecture.png" alt="GHOSTRAVEN system architecture" width="880"/>
<br/><sub>GHOSTRAVEN system architecture — intake, scoring, lab, evidence, defense, and action layers</sub>
</div>

### 🔗 Component Map

```mermaid
flowchart TB
    subgraph Intake["📋 Asset Intake"]
        A1[Crypto Asset Passport Builder]
    end

    subgraph Scoring["📊 Prioritization Engine"]
        B1[Quantum Exposure Scorer]
        B2[Dependency Blast-Radius Mapper]
        B3[Migration Urgency Ranker]
    end

    subgraph Lab["🧪 Synthetic Recovery Lab"]
        C1[Synthetic Asset Generator]
        C2[Witness Derivation - HKDF-SHA-256]
        C3[Attacker Worker - Fixed Budget]
        C4[Control Suite: Positive / Negative / Canary]
    end

    subgraph Evidence["⛓️ Evidence Layer"]
        D1[Hash Chain + Merkle Root]
        D2[Digital Signatures]
        D3[Signed Evidence Receipt]
    end

    subgraph Defense["🛡️ Active Defense"]
        E1[Decoy Archives & Honeytokens]
        E2[Cryptographic Exoskeleton Gateway]
        E3[Residual-Risk Ledger]
    end

    subgraph Output["🎫 Action Layer"]
        F1[AI Analyst - Advisory]
        F2[Evidence-Linked Migration Ticket]
    end

    A1 --> B1 --> B2 --> B3 --> F2
    B3 --> C1 --> C2 --> C3 --> C4 --> D1 --> D2 --> D3 --> F2
    E1 --> E3
    E2 --> E3 --> F2
    D3 -.explains.-> F1 -.recommends.-> F2
```

### 🔄 End-to-End Execution Flow

```mermaid
sequenceDiagram
    participant Owner as Asset Owner
    participant Passport as Crypto Asset Passport
    participant Scorer as Urgency Scorer
    participant Lab as Synthetic Recovery Lab
    participant Evidence as Evidence Ledger
    participant Analyst as AI Analyst
    participant Ticket as Migration Ticket

    Owner->>Passport: Register asset (algo, lifetime, criticality...)
    Passport->>Scorer: Feed asset profile
    Scorer->>Scorer: Rank by exposure + impact + difficulty
    Scorer->>Lab: Trigger synthetic challenge for high-risk asset
    Lab->>Lab: Plant secret → derive witness → seal commitment
    Lab->>Lab: Clear secret → run fixed attacker → verify
    Lab->>Evidence: Submit result + controls
    Evidence->>Evidence: Hash-chain + Merkle-seal + sign
    Evidence-->>Analyst: Surface anomalies / gaps
    Analyst-->>Ticket: Recommend action (Exoskeleton / full migration)
    Evidence->>Ticket: Attach signed proof bundle
    Ticket->>Owner: Owner, deadline, retest schedule, retirement clock
```

### 🛡️ Cryptographic Exoskeleton (for legacy assets)

```mermaid
flowchart LR
    Legacy[🏚️ Legacy System<br/>cannot adopt PQC yet] --> Gate{🚪 Exoskeleton Gateway}
    Gate -->|Approved routes only| Internal[Internal Network]
    Gate -->|Hybrid/PQC tunnel| External[External Clients]
    Gate -->|Blocks| Bypass[❌ Direct exposure / downgrade attempts]
    Gate --> Ledger[📒 Residual-Risk Ledger]
    Ledger --> Ticket[🎫 Migration Ticket<br/>retest + deadline + retirement clock]
```

> **Analogy:** it's like placing a modern, monitored security gate around an old house with a weak door. The old door isn't magically repaired — but every outside attacker must now pass through a hardened, hybrid/PQC-protected checkpoint first, and every attempt to bypass it is logged.

### 🪜 The Challenge Ladder (Synthetic Recovery Lab)

| Rung | Difficulty | What it demonstrates |
|---|---|---|
| **R1** | ~28-bit | Baseline — confirms the lab, controls, and pipeline work end to end |
| **R2** | Harder | Shows meaningful attacker capability under the fixed budget |
| **R3** | Harder still | Shows where the budget starts to strain |
| **R4** | ~62-bit | The frontier — where the fixed attacker profile stalls out |

The **highest rung actually recovered**, under full controls, is the signed **Observed Recovery Frontier** — a specific, falsifiable, reproducible claim, not a marketing adjective.

### 📚 Documentation Links

| Resource | Link |
|---|---|
| Live Demo | https://charming-gaufre-637b90.netlify.app |
| API Specification (OpenAPI/Swagger) | `<add link once published>` |
| Setup Wiki | `<add link once published>` |
| Design Docs | `<add link once published>` |

---

## 3️⃣ Installation & Configuration

### ✅ Prerequisites & Tech Stack

| Requirement | Version / Spec |
|---|---|
| Python | `>= 3.11` |
| Node.js *(if dashboard/API gateway uses it)* | `>= 20.x` |
| GPU | CUDA-capable GPU recommended for recovery workers *(CPU fallback supported for low ladder rungs)* |
| Memory | `>= 8 GB RAM` recommended |
| OS | Linux / macOS / WSL2 |

**Core stack:** Python · HKDF-SHA-256 · Hash-chain + Merkle-tree evidence logger · GPU recovery workers · Netlify (demo frontend)

### ⚙️ Step-by-Step Installation

```bash
# 1. Clone the repository
git clone <your-repo-url>
cd ghostraven

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy environment template and configure
cp .env.example .env

# 5. Initialize the evidence ledger (hash-chain + Merkle store)
python manage.py init-ledger

# 6. Run the synthetic recovery lab
python run_lab.py --config config/default.yaml

# 7. (Optional) Launch the dashboard
python app.py
```

### 🔑 Environment Variables Matrix

| Variable | Type | Default | Required | Description |
|---|---|---|:---:|---|
| `GHOSTRAVEN_ENV` | `string` | `development` | ✅ | Runtime environment (`development`, `staging`, `production`) |
| `ATTACKER_PROFILE_HARDWARE` | `string` | `single-gpu` | ✅ | Fixed hardware class for the recovery worker |
| `ATTACKER_PROFILE_HOURS` | `int` | `24` | ✅ | Fixed time budget (hours) for a challenge run |
| `ATTACKER_PROFILE_ENERGY_WATTHRS` | `int` | `500` | ✅ | Fixed energy budget per run |
| `WITNESS_KDF` | `string` | `HKDF-SHA-256` | ✅ | Key derivation function for session-bound witnesses |
| `EVIDENCE_SIGNING_KEY_PATH` | `path` | — | ✅ | Path to the private key used to sign evidence receipts |
| `MERKLE_STORE_PATH` | `path` | `./data/ledger` | ✅ | Local path for the hash-chain + Merkle evidence store |
| `HONEYTOKEN_ENABLED` | `bool` | `true` | ❌ | Toggles decoy archive / honeytoken deployment |
| `EXOSKELETON_GATEWAY_URL` | `url` | — | ❌ | Endpoint for the Cryptographic Exoskeleton gateway |
| `AI_ANALYST_API_KEY` | `secret` | — | ❌ | API key for the advisory AI analyst (explanations only, non-authoritative) |
| `TICKET_RETEST_INTERVAL_DAYS` | `int` | `90` | ❌ | Default retest cadence written to migration tickets |
| `LOG_LEVEL` | `string` | `info` | ❌ | Logging verbosity |

> ⚠️ Replace placeholder values with your actual repo's config keys before submission.

---

## 4️⃣ Developer Experience & Quality Control

### 💻 Usage Snippets

**Register an asset in the Crypto Asset Passport:**

```python
from ghostraven.passport import CryptoAssetPassport

passport = CryptoAssetPassport(
    asset_id="satcom-link-07",
    algorithm="RSA-2048",
    protocol="TLS 1.2",
    secrecy_lifetime_years=15,
    criticality="high",
    owner="network-infra-team",
    pqc_ready=False,
)

urgency = passport.score_urgency()
print(f"Migration urgency: {urgency.rank} ({urgency.score}/100)")
```

**Run a controlled recovery-frontier challenge:**

```bash
ghostraven lab run \
  --asset-profile satcom-link-07 \
  --ladder 28,34,48,62 \
  --attacker-profile single-gpu-24h \
  --output ./reports/satcom-link-07.json
```

**Verify a signed evidence receipt:**

```bash
ghostraven evidence verify ./reports/satcom-link-07.json
# ✔ Hash chain intact
# ✔ Merkle root matches
# ✔ Signature valid
# Status: Verified
```

**Deploy a Cryptographic Exoskeleton around a legacy asset:**

```bash
ghostraven exoskeleton deploy \
  --legacy-asset payroll-db-legacy \
  --mode hybrid-pqc-tunnel \
  --retest-days 90
```

**Query the prioritized migration list:**

```bash
ghostraven passport rank --top 10
# 1. satcom-link-07     | urgency: 94/100 | RSA-2048 | 15yr secrecy
# 2. legacy-payroll-db  | urgency: 88/100 | 3DES     | 10yr secrecy
# ...
```

### 🧪 Testing & QA Commands

```bash
# Run full unit test suite
pytest tests/unit -v

# Run integration suite (requires lab + ledger running)
pytest tests/integration -v

# Lint
flake8 ghostraven/
black --check ghostraven/

# Static analysis / security scan
bandit -r ghostraven/
mypy ghostraven/

# Validate evidence-chain integrity on sample data
python scripts/validate_ledger.py --sample
```

---

## 5️⃣ Reliability, Performance & Security

### 📈 Maturity & Benchmarks

| Status | Meaning |
|---|---|
| 🟠 **Alpha** | Core lab, evidence chain, and passport scoring implemented; dashboard and Exoskeleton gateway in active development |

| Metric | Current (illustrative — replace with real measured numbers) |
|---|---|
| Ladder rungs correctly detected | `4 / 4` |
| False leakage-canary hits | `0` |
| Evidence chain verification | `100%` reproducible |
| Avg. witness derivation latency | `< 50 ms` |
| Avg. challenge run (single GPU, R1–R4) | `~ <fill in> hours` |

### 🩹 Troubleshooting & Known Limitations

| Issue | Cause | Workaround / Trade-off |
|---|---|---|
| `Evidence: Contaminated` label on a run | A control (positive/negative/canary) failed during the run | Re-run with a clean environment; check `WITNESS_KDF` and clock sync before retrying |
| GPU worker fails to start | Missing CUDA drivers or GPU busy | Fall back to CPU mode (`--attacker-profile cpu-small`) for low-rung ladders only |
| Exoskeleton gateway reports `downgrade-attempt` false positives | Overly strict anti-downgrade policy on first deploy | Tune `EXOSKELETON_GATEWAY_URL` policy thresholds in `config/exoskeleton.yaml` |
| AI Analyst gives inconsistent explanations | Model is advisory-only and non-deterministic by design | Trust only the deterministic `Verified / Inconclusive / Contaminated / Invalid` label, never the AI narrative, for compliance decisions |
| Ledger write fails under concurrent runs | No current support for concurrent writers to one Merkle store | Run one lab instance per `MERKLE_STORE_PATH`, or shard by asset ID |

**Known limitation (stated plainly, not hidden):** GHOSTRAVEN measures a *declared laboratory attacker's* recovery capability under fixed, disclosed resources — it does **not** measure a real-world adversary's hidden compute power. Treat every Observed Recovery Frontier as a calibrated proxy for prioritization, not a universal guarantee that a real system is unbreakable.

### 🔐 Security Reporting

> 🙏 We take security seriously, especially for a tool built to reason about cryptographic risk.

- **Do not** open a public GitHub issue for a vulnerability.
- Report privately to: `<security-contact-email>`
- Please include: affected component, reproduction steps, and potential impact.
- We aim to acknowledge reports within **48 hours** and provide a remediation timeline within **5 business days**.

---

## 6️⃣ Governance & License

### 📜 License

This project is released under the **`<choose a license — e.g. MIT / Apache-2.0>`** license. See [`LICENSE`](./LICENSE) for full terms.

### 🤝 Contributing

1. Fork the repo and create a feature branch: `git checkout -b feature/your-feature`
2. Follow the code style: `black` + `flake8` must pass before a PR
3. Add or update tests for any behavior change
4. Open a PR describing the change and linking any related issue

### 🎨 Code Style

- **Python:** `black` formatting, `flake8` linting, type hints checked with `mypy`
- **Commits:** Conventional Commits style preferred (`feat:`, `fix:`, `docs:`...)
- **No real data, ever:** any PR touching the Synthetic Recovery Lab must use generated/synthetic assets only — never real credentials, keys, or production data

---

## 🏆 Why This Should Win

| Judging lens | How GHOSTRAVEN answers it |
|---|---|
| **Novelty** | Most PQC tools stop at "scan for weak algorithms." GHOSTRAVEN goes further: it *measures* recoverability under a disclosed attacker budget and turns that into a signed, auditable artifact — a category that barely exists today. |
| **Technical depth** | Session-bound witnesses (HKDF-SHA-256), commit-then-clear evidence flow, split-control (generate/seal/attack/verify kept separate), hash-chain + Merkle-sealed audit trail, and a deterministic (non-AI) validity gate. |
| **Real-world relevance** | HNDL is an active, documented concern across defense, finance, and healthcare today — not a hypothetical future problem. |
| **Responsible design** | Zero real data touched, zero real algorithms attacked, by architecture — not by policy promise. The system is safe to run against production-adjacent environments precisely because it never operates on real secrets. |
| **Completeness of the idea** | It doesn't stop at "here's your risk score." It closes the loop: Passport → Score → Measure → Evidence → Protect (Exoskeleton) → Track (Residual-Risk Ledger) → Ticket with a retirement clock. |
| **Honesty about limits** | We explicitly document what GHOSTRAVEN does *not* measure (a real adversary's hidden capability) instead of overselling the result — which is itself part of the evidentiary rigor we're pitching. |

---

## ❓ Judge FAQ

<details>
<summary><b>Does GHOSTRAVEN actually break real encryption?</b></summary>
<br/>
No — by design. Every recovery attempt runs against synthetic, lab-generated secrets that mimic a real asset's shape. GHOSTRAVEN never attacks real AES-256, RSA, ECC, or PQC algorithms, and never touches real customer data.
</details>

<details>
<summary><b>So what does the "Observed Recovery Frontier" actually prove?</b></summary>
<br/>
It proves what a specific, disclosed attacker profile (fixed hardware, time, energy, and method) could recover within a fixed budget, against a synthetic challenge of known difficulty. It's a calibrated, reproducible proxy for prioritization — not a claim about any real adversary's hidden capability.
</details>

<details>
<summary><b>Why not just use a standard PQC-readiness scanner?</b></summary>
<br/>
Scanners tell you an algorithm is "weak" in the abstract. GHOSTRAVEN adds the missing dimension: urgency. By combining the Crypto Asset Passport (secrecy lifetime, criticality, dependency blast radius) with a measured recovery frontier, it answers "weak compared to what, and how soon does it matter" — the actual question a migration budget needs answered.
</details>

<details>
<summary><b>What happens to a legacy system that can't adopt PQC right away?</b></summary>
<br/>
It gets wrapped in a Cryptographic Exoskeleton: a modern gateway that restricts it to approved routes, blocks direct exposure, detects bypass/downgrade attempts, and opens hybrid/PQC tunnels for external traffic. Remaining risk is tracked in the Residual-Risk Ledger, and an evidence-linked migration ticket keeps a hard deadline and retirement clock so the Exoskeleton never becomes a permanent excuse.
</details>

<details>
<summary><b>Why have an AI analyst at all if it's not trusted for validity?</b></summary>
<br/>
Because the hard part of security tooling isn't just generating evidence — it's getting a human to read and act on it quickly. The AI analyst explains anomalies, missing evidence, and migration trade-offs in plain language. But the labels that actually matter (`Verified`, `Inconclusive`, `Contaminated`, `Invalid`) are decided entirely by deterministic cryptographic checks, never by the model.
</details>

<details>
<summary><b>How do we know the evidence hasn't been tampered with?</b></summary>
<br/>
Every step — plant, seal, attack, verify — is hash-chained and sealed into a Merkle tree, then digitally signed. Any after-the-fact edit to a report breaks the hash chain or the signature, making tampering mathematically detectable rather than just policy-forbidden.
</details>

---

## 👥 Team

**Team KARMIN** · ASYNC 2026 · Cybersecurity & Defense Track

| Role | Name / USN |
|---|---|
| Team Lead | Abhinava N. |
| Members | 1MS25IM003 · 1MS25AS002 · 1MS25IS106 · 1MS25IS133 |

---

<div align="center">

### 👻 GHOSTRAVEN

**Replacing belief about quantum risk with signed, reproducible evidence.**

[![Live Demo](https://img.shields.io/badge/🔗_Try_the_Demo-charming--gaufre--637b90.netlify.app-black?style=for-the-badge)](https://charming-gaufre-637b90.netlify.app)

*Built for ASYNC 2026.*

</div>
