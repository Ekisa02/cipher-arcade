from pydantic import BaseModel, Field
from typing import Optional, Dict, Any

class KeyPairResponse(BaseModel):
    private_key: str
    public_key: str
    address: str

class SignRequest(BaseModel):
    private_key: str
    message: str

class SignResponse(BaseModel):
    signature: str

class VerifyRequest(BaseModel):
    public_key: str
    message: str
    signature: str

class VerifyResponse(BaseModel):
    valid: bool

class TxRequest(BaseModel):
    from_addr: str = Field(..., alias="from")
    to: str
    amount: float
    metadata: Optional[Dict[str, Any]] = None

class TxResponse(BaseModel):
    txid: str
    anomaly_score: float
    flagged: bool

