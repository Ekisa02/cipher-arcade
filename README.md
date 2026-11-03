# Cipher Arcade

Cipher Arcade is a modular FastAPI + PyTorch toolkit providing blockchain & crypto utilities: keypair management, signing/verification, transaction simulation, a lightweight in-memory chain simulator, and a PyTorch-based anomaly detector for transaction analysis.

The project is organized for clarity and extensibility so you can use the crypto utilities as a library, run a local API for integration, or extend the ML model for production research.

## Highlights
- FastAPI HTTP endpoints for common crypto operations (key generation, signing, verification, tx simulation)
- ECDSA (secp256k1) key utilities
- Lightweight transaction simulator and chain state module
- PyTorch anomaly detector with simple training script and inference API
- Tests with pytest and example usage

## Architecture

- app/
  - main.py          -> FastAPI application entry (mounts routers)
  - api/             -> HTTP route definitions
  - core/            -> core blockchain & crypto utilities
  - ml/              -> PyTorch model, training & inference utilities
  - schemas.py       -> Pydantic models for API validation
  - config.py        -> configuration and constants
- tests/             -> pytest test suites
- docs/              -> API & design docs

Flow examples:
- Key generation -> sign messages -> verify signatures
- Create a simulated transaction -> run anomaly detection -> accept/reject

## Installation

1. Clone:

   git clone https://github.com/your-org/cipher-arcade.git
   cd cipher-arcade

2. Create venv & install dependencies:

   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt

3. (Optional) Train small demo model for anomaly detection

   python -m app.ml.train --epochs 5

4. Run the API server:

   uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

5. API docs available at
   - OpenAPI: http://127.0.0.1:8000/docs
   - ReDoc:   http://127.0.0.1:8000/redoc

## Usage examples

Generate a keypair:

curl -X POST "http://127.0.0.1:8000/keys/generate" -H "Content-Type: application/json"

Sign a message:

curl -X POST "http://127.0.0.1:8000/sign" -H "Content-Type: application/json" -d '{"private_key": "<hex>", "message": "hello"}'

Verify:

curl -X POST "http://127.0.0.1:8000/verify" -H "Content-Type: application/json" -d '{"public_key": "<hex>", "message":"hello", "signature":"<hex>"}'

Simulate a transaction and run anomaly detection:

curl -X POST "http://127.0.0.1:8000/tx/simulate" -H "Content-Type: application/json" -d '{"from":"<addr>", "to":"<addr>", "amount": 5.0, "metadata": {}}'

## Tests

Run tests with:

   pytest -q

## Extending
- Add more crypto algorithms in app/core
- Replace anomaly model with richer dataset and architecture in app/ml
- Swap in persistent storage adapter for the chain simulator in app/core/storage.py

## License
MIT
