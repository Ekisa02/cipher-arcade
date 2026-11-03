from fastapi import APIRouter, HTTPException
from app.schemas import *
from app.core import crypto, chain
from app.ml.predict import predict_tx_anomaly

router = APIRouter()

@router.post("/keys/generate", response_model=KeyPairResponse)
async def generate_keys():
    priv, pub = crypto.generate_keypair()
    address = crypto.pubkey_to_address(pub)
    return {"private_key": priv, "public_key": pub, "address": address}

@router.post("/sign", response_model=SignResponse)
async def sign(req: SignRequest):
    try:
        signature = crypto.sign_message(req.private_key, req.message)
        return {"signature": signature}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.post("/verify", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    valid = crypto.verify_signature(req.public_key, req.message, req.signature)
    return {"valid": valid}

@router.post("/tx/simulate", response_model=TxResponse)
async def simulate_tx(tx: TxRequest):
    # simple simulated transaction creation
    txid = chain.create_transaction(tx.from_addr, tx.to, tx.amount, tx.metadata or {})
    # compute features and run anomaly detection
    score = predict_tx_anomaly({
        "amount": float(tx.amount),
        "from_entropy": float(len(tx.from_addr) % 10),
        "to_entropy": float(len(tx.to) % 10)
    })
    flagged = score > 0.6
    return {"txid": txid, "anomaly_score": float(score), "flagged": bool(flagged)}
