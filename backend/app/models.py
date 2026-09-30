from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field

class WitnessStatus(str, Enum):
    VALID = "VALID"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    INVALIDATED = "INVALIDATED"

class RungStatus(str, Enum):
    HUNTING = "HUNTING"
    RECOVERING = "RECOVERING"
    RECONSTRUCTED = "RECONSTRUCTED"
    VERIFYING = "VERIFYING"
    VERIFIED = "VERIFIED"
    REJECTED = "REJECTED"
    BUDGET_EXHAUSTED = "BUDGET_EXHAUSTED"

class ExperimentStatus(str, Enum):
    CREATED = "CREATED"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    INVALIDATED = "INVALIDATED"

class ControlStatus(str, Enum):
    OK = "OK"
    BREACHED = "BREACHED"

class ChallengeRung(BaseModel):
    rung_id: str
    bits: int
    status: RungStatus = RungStatus.HUNTING
    recovered: bool = False
    candidate_secret: Optional[str] = None
    witness_status: WitnessStatus = WitnessStatus.PENDING
    verification_time_ms: float = 0.0
    attack_budget_spent: float = 0.0

class Control(BaseModel):
    id: str
    type: str
    status: ControlStatus = ControlStatus.OK
    details: str

class EvidenceEntry(BaseModel):
    index: int
    timestamp: str
    event_type: str
    rung_id: Optional[str] = None
    payload: Dict[str, Any]
    prev_hash: str
    hash: str

class Experiment(BaseModel):
    id: str
    created_at: str
    status: ExperimentStatus = ExperimentStatus.CREATED
    rungs: List[ChallengeRung]
    controls: List[Control]
    frontier: str = "NONE"  # "NONE", "R1", "R2", "R3", "R4", "WITHHELD"
    invalidated: bool = False
    invalidation_reason: Optional[str] = None
    adaptive_eligible: bool = False
    active_secret_cleared: bool = True
    commitment_hash: str
    witness_binding_id: str
    mock_mode: bool = False

class ExposureMetrics(BaseModel):
    experiment_id: str
    frontier: str
    verified_rungs_count: int
    max_bit_depth_recovered: int
    overall_risk_level: str
    summary: str
    invalidation_reason: Optional[str] = None

class AdaptiveChallengeRequest(BaseModel):
    target_rung: Optional[str] = "R5"
    custom_budget_sec: Optional[float] = 60.0

class AdaptiveChallengeResponse(BaseModel):
    experiment_id: str
    adaptive_challenge_id: str
    status: str
    target_rung: str
    bit_depth: int
    message: str
