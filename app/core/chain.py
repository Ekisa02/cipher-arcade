import uuid
from typing import Dict, Any

# In-memory minimal chain state for demo purposes
CHAIN: Dict[str, Dict[str, Any]] = {}


def create_transaction(from_addr: str, to: str, amount: float, metadata: Dict[str, Any]) -> str:
    txid = uuid.uuid4().hex
    CHAIN[txid] = {
        "from": from_addr,
        "to": to,
        "amount": amount,
        "metadata": metadata,
    }
    return txid


def get_transaction(txid: str):
    return CHAIN.get(txid)
