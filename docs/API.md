# API Reference (Cipher Arcade)

## /health
GET: returns application health.

## /keys/generate
POST: generate a keypair. Returns private_key (hex), public_key (hex), address.

## /sign
POST: sign a message
- body: { private_key: <hex>, message: <string> }
- response: { signature: <hex> }

## /verify
POST: verify signature
- body: { public_key: <hex>, message: <string>, signature: <hex> }
- response: { valid: true|false }

## /tx/simulate
POST: simulate a transaction and run anomaly detection
- body: { "from": <address>, "to": <address>, "amount": <float>, "metadata": { ... } }
- response: { txid: <id>, anomaly_score: <0..1>, flagged: bool }
