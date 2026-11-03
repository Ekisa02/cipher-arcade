# Design Notes

- Crypto: ECDSA over secp256k1 (using ecdsa library). Keys and signatures are hex-encoded strings for ease of transport.
- Address: simplified SHA256-based address for demo; replace with real encoding (RIPEMD160 + base58 / bech32) for production.
- Chain: in-memory dictionary for prototyping; replace with DB (SQLite / LevelDB) and block/consensus logic if needed.
- ML: small PyTorch model that demonstrates integrating ML inference into the API pipeline. Replace synthetic data and train on real telemetry for production.

Security notes:
- Private keys should never be sent to untrusted services in production.
- This project is for prototyping and education; do not use as-is for storing real assets.
