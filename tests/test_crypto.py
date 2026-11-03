import pytest
from app.core import crypto


def test_key_generation_and_address():
    priv, pub = crypto.generate_keypair()
    assert isinstance(priv, str) and isinstance(pub, str)
    addr = crypto.pubkey_to_address(pub)
    assert addr.startswith('0x') and len(addr) > 2


def test_sign_and_verify():
    priv, pub = crypto.generate_keypair()
    msg = "unit test message"
    sig = crypto.sign_message(priv, msg)
    assert isinstance(sig, str)
    valid = crypto.verify_signature(pub, msg, sig)
    assert valid


def test_verify_invalid():
    priv, pub = crypto.generate_keypair()
    msg = "message"
    sig = crypto.sign_message(priv, msg)
    # tamper signature
    bad = sig[:-2] + ("00")
    assert not crypto.verify_signature(pub, msg, bad)
