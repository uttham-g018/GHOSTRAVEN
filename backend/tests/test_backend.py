import pytest
from fastapi.testclient import TestClient
from backend.app.main import app
from backend.app.experiment import ExperimentEngine
from backend.app.models import WitnessStatus, RungStatus, ExperimentStatus, ControlStatus

client = TestClient(app)

def test_1_health_check():
    response = client.get("/api/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["service"] == "ghostraven-backend"

def test_2_create_experiment():
    response = client.post("/api/experiments")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["status"] == ExperimentStatus.CREATED
    assert data["frontier"] == "NONE"
    assert len(data["rungs"]) == 4

def test_3_get_experiment():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    get_res = client.get(f"/api/experiments/{exp_id}")
    assert get_res.status_code == 200
    data = get_res.json()
    assert data["id"] == exp_id

def test_4_get_experiment_404():
    response = client.get("/api/experiments/invalid-exp-id-999")
    assert response.status_code == 404

def test_5_run_experiment():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    run_res = client.post(f"/api/experiments/{exp_id}/run")
    assert run_res.status_code == 200
    data = run_res.json()
    assert data["status"] == ExperimentStatus.COMPLETED
    assert data["frontier"] == "R2"
    assert data["rungs"][0]["status"] == RungStatus.VERIFIED
    assert data["rungs"][1]["status"] == RungStatus.VERIFIED
    assert data["rungs"][2]["status"] == RungStatus.BUDGET_EXHAUSTED
    assert data["rungs"][3]["status"] == RungStatus.BUDGET_EXHAUSTED

def test_6_poll_status():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    status_res = client.get(f"/api/experiments/{exp_id}/status")
    assert status_res.status_code == 200
    data = status_res.json()
    assert data["id"] == exp_id
    assert data["status"] == ExperimentStatus.COMPLETED
    assert data["frontier"] == "R2"
    assert data["adaptive_eligible"] is True

def test_7_get_frontier():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    frontier_res = client.get(f"/api/experiments/{exp_id}/frontier")
    assert frontier_res.status_code == 200
    data = frontier_res.json()
    assert data["frontier"] == "R2"
    assert data["invalidated"] is False

def test_8_get_evidence_chain():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    evidence_res = client.get(f"/api/experiments/{exp_id}/evidence")
    assert evidence_res.status_code == 200
    entries = evidence_res.json()
    assert len(entries) > 0
    event_types = [e["event_type"] for e in entries]
    assert "GENERATE" in event_types
    assert "BIND" in event_types
    assert "COMMIT" in event_types
    assert "CLEAR" in event_types
    assert "VERIFY" in event_types
    assert "MEASURE" in event_types

def test_9_adaptive_challenge_success():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    adaptive_res = client.post(f"/api/experiments/{exp_id}/adaptive-challenge", json={"target_rung": "R5", "custom_budget_sec": 60.0})
    assert adaptive_res.status_code == 200
    data = adaptive_res.json()
    assert data["target_rung"] == "R5"
    assert data["bit_depth"] == 74
    assert "SCHEDULED" in data["status"]

def test_10_invalid_witness_handling():
    # Force R2 to fail witness signature verification
    create_res = client.post("/api/experiments?force_invalid_witness_rung=R2").json()
    exp_id = create_res["id"]

    run_res = client.post(f"/api/experiments/{exp_id}/run").json()
    assert run_res["rungs"][1]["status"] == RungStatus.REJECTED
    assert run_res["rungs"][1]["witness_status"] == WitnessStatus.REJECTED
    # Frontier must be R1, NOT R2!
    assert run_res["frontier"] == "R1"

def test_11_control_breach_invalidation():
    # Force control breach
    create_res = client.post("/api/experiments?force_control_breach=true").json()
    exp_id = create_res["id"]

    run_res = client.post(f"/api/experiments/{exp_id}/run").json()
    assert run_res["status"] == ExperimentStatus.INVALIDATED
    assert run_res["invalidated"] is True
    assert run_res["frontier"] == "WITHHELD"
    assert run_res["invalidation_reason"] is not None
    assert "CONTROL BREACH" in run_res["invalidation_reason"]

def test_12_adaptive_challenge_disabled_on_invalidation():
    create_res = client.post("/api/experiments?force_control_breach=true").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    adaptive_res = client.post(f"/api/experiments/{exp_id}/adaptive-challenge", json={"target_rung": "R5"})
    assert adaptive_res.status_code == 400
    assert "withheld" in adaptive_res.json()["detail"].lower() or "invalidated" in adaptive_res.json()["detail"].lower()

def test_13_exposure_api():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    exposure_res = client.get(f"/api/exposure?experiment_id={exp_id}")
    assert exposure_res.status_code == 200
    data = exposure_res.json()
    assert data["frontier"] == "R2"
    assert data["max_bit_depth_recovered"] == 38
    assert data["overall_risk_level"] == "MODERATE"
    assert "Session-secret recovery was observed" in data["summary"]

def test_14_evidence_hash_chain_integrity():
    create_res = client.post("/api/experiments").json()
    exp_id = create_res["id"]

    client.post(f"/api/experiments/{exp_id}/run")
    ledger = ExperimentEngine.get_ledger(exp_id)
    assert ledger is not None
    assert ledger.verify_integrity() is True
