import hashlib
import hmac
import json
import time
from typing import Dict, Any

def hkdf_extract(salt: bytes, ikm: bytes) -> bytes:
    if not salt:
        salt = b"\x00" * 32
    return hmac.new(salt, ikm, hashlib.sha256).digest()

def hkdf_expand(prk: bytes, info: bytes, length: int = 32) -> bytes:
    t = b""
    okm = b""
    i = 1
    while len(okm) < length:
        t = hmac.new(prk, t + info + bytes([i]), hashlib.sha256).digest()
        okm += t
        i += 1
    return okm[:length]

def derive_hkdf_sha256(secret: str, salt: str, info: str, length: int = 32) -> str:
    prk = hkdf_extract(salt.encode('utf-8'), secret.encode('utf-8'))
    okm = hkdf_expand(prk, info.encode('utf-8'), length)
    return okm.hex()

def derive_session_witness(session_id: str, rung_id: str, experiment_id: str, candidate_secret: str) -> str:
    """
    Derives HKDF-SHA256 witness bound to session, rung, experiment identity and candidate secret.
    """
    info = f"GHOSTRAVEN-WITNESS:{session_id}:{experiment_id}:{rung_id}"
    salt = f"GHOSTRAVEN-SALT:{experiment_id}"
    return derive_hkdf_sha256(candidate_secret, salt, info, length=32)

def verify_witness_signature(
    session_id: str,
    rung_id: str,
    experiment_id: str,
    candidate_secret: str,
    expected_witness: str
) -> bool:
    """
    Verifies derived witness against expected commitment witness.
    """
    derived = derive_session_witness(session_id, rung_id, experiment_id, candidate_secret)
    return hmac.compare_digest(derived, expected_witness)

def calculate_commitment(session_id: str, experiment_id: str, timestamp: str) -> str:
    raw = f"COMMITMENT:{session_id}:{experiment_id}:{timestamp}"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()

def compute_hash_chain_entry(index: int, prev_hash: str, event_type: str, payload: Dict[str, Any]) -> str:
    serialized_payload = json.dumps(payload, sort_keys=True)
    raw = f"{index}:{prev_hash}:{event_type}:{serialized_payload}"
    return hashlib.sha256(raw.encode('utf-8')).hexdigest()
