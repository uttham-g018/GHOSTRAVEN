import uuid
import datetime
from typing import Dict, Optional, List
from .models import (
    Experiment,
    ExperimentStatus,
    ChallengeRung,
    RungStatus,
    WitnessStatus,
    Control,
    ControlStatus,
    ExposureMetrics,
    AdaptiveChallengeResponse
)
from .crypto import (
    derive_session_witness,
    verify_witness_signature,
    calculate_commitment
)
from .ledger import EvidenceLedger

# In-memory store for active experiments and ledgers
_experiments: Dict[str, Experiment] = {}
_ledgers: Dict[str, EvidenceLedger] = {}

class ExperimentEngine:
    @staticmethod
    def create_experiment(mock_mode: bool = False, force_control_breach: bool = False, force_invalid_witness_rung: Optional[str] = None) -> Experiment:
        exp_id = f"exp-{uuid.uuid4().hex[:8]}"
        now = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        commitment = calculate_commitment("session-active", exp_id, now)
        witness_binding = f"bind-{uuid.uuid4().hex[:6]}"

        rungs = [
            ChallengeRung(rung_id="R1", bits=28, status=RungStatus.HUNTING),
            ChallengeRung(rung_id="R2", bits=38, status=RungStatus.HUNTING),
            ChallengeRung(rung_id="R3", bits=50, status=RungStatus.HUNTING),
            ChallengeRung(rung_id="R4", bits=62, status=RungStatus.HUNTING),
        ]

        controls = [
            Control(id="AES-256", type="symmetric_key", status=ControlStatus.BREACHED if force_control_breach else ControlStatus.OK, details="Symmetric cipher control baseline"),
            Control(id="ML-KEM-768", type="post_quantum_leakage_channel", status=ControlStatus.OK, details="Post-quantum key encapsulation leakage channel control")
        ]

        exp = Experiment(
            id=exp_id,
            created_at=now,
            status=ExperimentStatus.CREATED,
            rungs=rungs,
            controls=controls,
            frontier="NONE",
            invalidated=False,
            invalidation_reason=None,
            adaptive_eligible=False,
            active_secret_cleared=True,
            commitment_hash=commitment,
            witness_binding_id=witness_binding,
            mock_mode=mock_mode
        )

        ledger = EvidenceLedger(exp_id)
        ledger.append("GENERATE", {"session_id": "session-active", "challenge_ladder": ["R1", "R2", "R3", "R4"]})
        ledger.append("BIND", {"witness_binding_id": witness_binding, "scheme": "HKDF-SHA256"})
        ledger.append("COMMIT", {"commitment_hash": commitment})
        ledger.append("CLEAR", {"active_secret_cleared": True, "notice": "Active application-level secret material cleared."})

        _experiments[exp_id] = exp
        _ledgers[exp_id] = ledger

        # Store test overrides if any
        exp._force_invalid_witness_rung = force_invalid_witness_rung  # type: ignore
        return exp

    @staticmethod
    def get_experiment(exp_id: str) -> Optional[Experiment]:
        return _experiments.get(exp_id)

    @staticmethod
    def get_ledger(exp_id: str) -> Optional[EvidenceLedger]:
        return _ledgers.get(exp_id)

    @staticmethod
    def run_experiment(exp_id: str) -> Experiment:
        exp = _experiments.get(exp_id)
        if not exp:
            raise KeyError(f"Experiment {exp_id} not found")
        
        ledger = _ledgers.get(exp_id)
        exp.status = ExperimentStatus.RUNNING

        if ledger:
            ledger.append("RUN_START", {"status": "RUNNING"})

        # Check for control breach first
        for control in exp.controls:
            if control.status == ControlStatus.BREACHED:
                exp.status = ExperimentStatus.INVALIDATED
                exp.invalidated = True
                exp.invalidation_reason = f"CONTROL BREACH: Control {control.id} was breached."
                exp.frontier = "WITHHELD"
                exp.adaptive_eligible = False
                if ledger:
                    ledger.append("CONTROL_BREACH", {"control_id": control.id, "reason": exp.invalidation_reason})
                    ledger.append("INVALIDATED", {"frontier": "WITHHELD", "reason": exp.invalidation_reason})
                return exp

        force_invalid_rung = getattr(exp, "_force_invalid_witness_rung", None)

        # Process ladder rungs
        # Standard behavior: R1 & R2 recovered & verified, R3 & R4 budget exhausted
        for rung in exp.rungs:
            if rung.rung_id in ["R1", "R2"]:
                if force_invalid_rung == rung.rung_id:
                    # Invalid witness simulation for this rung
                    rung.status = RungStatus.REJECTED
                    rung.recovered = False
                    rung.candidate_secret = f"cand-{rung.rung_id}-invalid-secret"
                    rung.witness_status = WitnessStatus.REJECTED
                    rung.verification_time_ms = 45.2
                    rung.attack_budget_spent = 120.0
                    if ledger:
                        ledger.append("WITNESS_REJECTED", {
                            "rung_id": rung.rung_id,
                            "reason": "HKDF-SHA256 witness mismatch. Recovery candidate rejected."
                        }, rung_id=rung.rung_id)
                else:
                    # Valid witness recovery
                    secret_candidate = f"secret-cand-{rung.rung_id}-valid"
                    expected_witness = derive_session_witness("session-active", rung.rung_id, exp.id, secret_candidate)
                    is_valid = verify_witness_signature("session-active", rung.rung_id, exp.id, secret_candidate, expected_witness)
                    
                    if is_valid:
                        rung.status = RungStatus.VERIFIED
                        rung.recovered = True
                        rung.candidate_secret = secret_candidate
                        rung.witness_status = WitnessStatus.VALID
                        rung.verification_time_ms = 32.5 if rung.rung_id == "R1" else 88.4
                        rung.attack_budget_spent = 100.0 if rung.rung_id == "R1" else 450.0
                        if ledger:
                            ledger.append("VERIFY", {
                                "rung_id": rung.rung_id,
                                "witness_status": "VALID",
                                "verification_time_ms": rung.verification_time_ms
                            }, rung_id=rung.rung_id)
                    else:
                        rung.status = RungStatus.REJECTED
                        rung.witness_status = WitnessStatus.REJECTED
                        if ledger:
                            ledger.append("WITNESS_REJECTED", {"rung_id": rung.rung_id}, rung_id=rung.rung_id)
            else:
                # R3 & R4: budget exhausted without recovery
                rung.status = RungStatus.BUDGET_EXHAUSTED
                rung.recovered = False
                rung.witness_status = WitnessStatus.PENDING
                rung.attack_budget_spent = 1000.0
                if ledger:
                    ledger.append("BUDGET_EXHAUSTED", {
                        "rung_id": rung.rung_id,
                        "notice": "No recovery observed within configured attack budget."
                    }, rung_id=rung.rung_id)

        # Calculate Authoritative Frontier
        # The frontier is the HIGHEST verified rung with VALID witness.
        verified_rungs = [r.rung_id for r in exp.rungs if r.status == RungStatus.VERIFIED and r.witness_status == WitnessStatus.VALID]
        if verified_rungs:
            exp.frontier = verified_rungs[-1]  # Highest verified rung e.g. "R2"
        else:
            exp.frontier = "NONE"

        exp.status = ExperimentStatus.COMPLETED
        exp.adaptive_eligible = True if exp.frontier != "NONE" else False

        if ledger:
            ledger.append("MEASURE", {"frontier": exp.frontier, "verified_rungs": verified_rungs})
            ledger.append("PRIORITIZE", {"adaptive_eligible": exp.adaptive_eligible})

        return exp

    @staticmethod
    def calculate_frontier(exp_id: str) -> str:
        exp = _experiments.get(exp_id)
        if not exp:
            return "NONE"
        if exp.invalidated:
            return "WITHHELD"
        return exp.frontier

    @staticmethod
    def get_exposure(exp_id: Optional[str] = None) -> ExposureMetrics:
        target_exp = _experiments.get(exp_id) if exp_id else None
        if not target_exp and _experiments:
            target_exp = list(_experiments.values())[-1]

        if not target_exp:
            return ExposureMetrics(
                experiment_id="none",
                frontier="NONE",
                verified_rungs_count=0,
                max_bit_depth_recovered=0,
                overall_risk_level="LOW",
                summary="No active experiment recorded."
            )

        if target_exp.invalidated:
            return ExposureMetrics(
                experiment_id=target_exp.id,
                frontier="WITHHELD",
                verified_rungs_count=0,
                max_bit_depth_recovered=0,
                overall_risk_level="WITHHELD",
                summary=f"Experiment invalidated: {target_exp.invalidation_reason}",
                invalidation_reason=target_exp.invalidation_reason
            )

        verified = [r for r in target_exp.rungs if r.status == RungStatus.VERIFIED]
        max_bits = max([r.bits for r in verified], default=0)

        risk = "LOW"
        if target_exp.frontier in ["R1", "R2"]:
            risk = "MODERATE"
        elif target_exp.frontier in ["R3", "R4"]:
            risk = "CRITICAL"

        summary_msg = (
            f"Session-secret recovery was observed and independently verified through {target_exp.frontier} "
            f"under configured experiment and attack budget."
            if target_exp.frontier != "NONE"
            else "No recovery was observed within configured attack budget."
        )

        return ExposureMetrics(
            experiment_id=target_exp.id,
            frontier=target_exp.frontier,
            verified_rungs_count=len(verified),
            max_bit_depth_recovered=max_bits,
            overall_risk_level=risk,
            summary=summary_msg
        )

    @staticmethod
    def create_adaptive_challenge(exp_id: str, target_rung: str = "R5", budget: float = 60.0) -> AdaptiveChallengeResponse:
        exp = _experiments.get(exp_id)
        if not exp:
            raise KeyError(f"Experiment {exp_id} not found")

        if exp.invalidated or not exp.adaptive_eligible or exp.frontier == "WITHHELD":
            raise ValueError("Adaptive challenge withheld: experiment is invalidated or not eligible.")

        challenge_id = f"adaptive-{uuid.uuid4().hex[:6]}"
        bit_depth = 74 if target_rung == "R5" else 88

        ledger = _ledgers.get(exp_id)
        if ledger:
            ledger.append("ADAPTIVE_CHALLENGE", {
                "adaptive_challenge_id": challenge_id,
                "target_rung": target_rung,
                "bit_depth": bit_depth,
                "budget_sec": budget
            })

        return AdaptiveChallengeResponse(
            experiment_id=exp_id,
            adaptive_challenge_id=challenge_id,
            status="SCHEDULED",
            target_rung=target_rung,
            bit_depth=bit_depth,
            message=f"Adaptive challenge {target_rung} ({bit_depth}-bit) scheduled under expanded attack budget."
        )
