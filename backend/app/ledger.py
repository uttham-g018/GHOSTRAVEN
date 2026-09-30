import datetime
from typing import List, Dict, Any, Optional
from .models import EvidenceEntry
from .crypto import compute_hash_chain_entry

GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

class EvidenceLedger:
    def __init__(self, experiment_id: str):
        self.experiment_id = experiment_id
        self.entries: List[EvidenceEntry] = []
        # Append genesis event
        self.append("GENESIS", payload={"experiment_id": experiment_id, "status": "INITIALIZED"})

    def append(self, event_type: str, payload: Dict[str, Any], rung_id: Optional[str] = None) -> EvidenceEntry:
        index = len(self.entries)
        prev_hash = self.entries[-1].hash if index > 0 else GENESIS_HASH
        timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
        
        entry_hash = compute_hash_chain_entry(index, prev_hash, event_type, payload)
        
        entry = EvidenceEntry(
            index=index,
            timestamp=timestamp,
            event_type=event_type,
            rung_id=rung_id,
            payload=payload,
            prev_hash=prev_hash,
            hash=entry_hash
        )
        self.entries.append(entry)
        return entry

    def verify_integrity(self) -> bool:
        for i, entry in enumerate(self.entries):
            expected_prev = self.entries[i-1].hash if i > 0 else GENESIS_HASH
            if entry.prev_hash != expected_prev:
                return False
            recomputed = compute_hash_chain_entry(entry.index, entry.prev_hash, entry.event_type, entry.payload)
            if entry.hash != recomputed:
                return False
        return True

    def get_entries(self) -> List[EvidenceEntry]:
        return list(self.entries)
