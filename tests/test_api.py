import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'ok'


def test_key_endpoints():
    r = client.post('/keys/generate')
    assert r.status_code == 200
    body = r.json()
    assert 'private_key' in body and 'public_key' in body and 'address' in body

    # sign and verify via API
    sign_resp = client.post('/sign', json={"private_key": body['private_key'], "message": "hi"})
    assert sign_resp.status_code == 200
    sig = sign_resp.json()['signature']
    verify_resp = client.post('/verify', json={"public_key": body['public_key'], "message": "hi", "signature": sig})
    assert verify_resp.status_code == 200
    assert verify_resp.json()['valid'] is True


def test_tx_simulate():
    # generate two addresses and simulate tx
    a = client.post('/keys/generate').json()['address']
    b = client.post('/keys/generate').json()['address']
    r = client.post('/tx/simulate', json={"from": a, "to": b, "amount": 1.5})
    assert r.status_code == 200
    j = r.json()
    assert 'txid' in j and 'anomaly_score' in j and 'flagged' in j
