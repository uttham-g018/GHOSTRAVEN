from fastapi import APIRouter, HTTPException, Query, Path
from typing import List, Optional, Dict, Any
from .models import (
    Experiment,
    EvidenceEntry,
    ExposureMetrics,
    AdaptiveChallengeRequest,
    AdaptiveChallengeResponse
)
from .experiment import ExperimentEngine

router = APIRouter(prefix="/api")

@router.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "ok", "service": "ghostraven-backend"}

@router.post("/experiments", response_model=Experiment)
def create_experiment(
    mock_mode: bool = Query(False),
    force_control_breach: bool = Query(False),
    force_invalid_witness_rung: Optional[str] = Query(None)
):
    exp = ExperimentEngine.create_experiment(
        mock_mode=mock_mode,
        force_control_breach=force_control_breach,
        force_invalid_witness_rung=force_invalid_witness_rung
    )
    return exp

@router.get("/experiments/{id}", response_model=Experiment)
def get_experiment(id: str = Path(...)):
    exp = ExperimentEngine.get_experiment(id)
    if not exp:
        raise HTTPException(status_code=404, detail=f"Experiment '{id}' not found.")
    return exp

@router.post("/experiments/{id}/run", response_model=Experiment)
def run_experiment(id: str = Path(...)):
    exp = ExperimentEngine.get_experiment(id)
    if not exp:
        raise HTTPException(status_code=404, detail=f"Experiment '{id}' not found.")
    try:
        updated_exp = ExperimentEngine.run_experiment(id)
        return updated_exp
    except KeyError as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/experiments/{id}/status")
def get_experiment_status(id: str = Path(...)):
    exp = ExperimentEngine.get_experiment(id)
    if not exp:
        raise HTTPException(status_code=404, detail=f"Experiment '{id}' not found.")
    return {
        "id": exp.id,
        "status": exp.status,
        "frontier": exp.frontier,
        "invalidated": exp.invalidated,
        "invalidation_reason": exp.invalidation_reason,
        "adaptive_eligible": exp.adaptive_eligible
    }

@router.get("/experiments/{id}/frontier")
def get_experiment_frontier(id: str = Path(...)):
    exp = ExperimentEngine.get_experiment(id)
    if not exp:
        raise HTTPException(status_code=404, detail=f"Experiment '{id}' not found.")
    return {
        "id": exp.id,
        "frontier": exp.frontier,
        "invalidated": exp.invalidated,
        "invalidation_reason": exp.invalidation_reason
    }

@router.get("/experiments/{id}/evidence", response_model=List[EvidenceEntry])
def get_experiment_evidence(id: str = Path(...)):
    ledger = ExperimentEngine.get_ledger(id)
    if not ledger:
        raise HTTPException(status_code=404, detail=f"Evidence ledger for experiment '{id}' not found.")
    return ledger.get_entries()

@router.post("/experiments/{id}/adaptive-challenge", response_model=AdaptiveChallengeResponse)
def trigger_adaptive_challenge(id: str = Path(...), req: Optional[AdaptiveChallengeRequest] = None):
    exp = ExperimentEngine.get_experiment(id)
    if not exp:
        raise HTTPException(status_code=404, detail=f"Experiment '{id}' not found.")
    
    target_rung = req.target_rung if req and req.target_rung else "R5"
    budget = req.custom_budget_sec if req and req.custom_budget_sec else 60.0

    try:
        res = ExperimentEngine.create_adaptive_challenge(id, target_rung=target_rung, budget=budget)
        return res
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/exposure", response_model=ExposureMetrics)
def get_exposure(experiment_id: Optional[str] = Query(None)):
    return ExperimentEngine.get_exposure(experiment_id)
