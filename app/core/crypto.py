import os
import hashlib
from ecdsa import SigningKey, SECP256k1, VerifyingKey, BadSignatureError
import binascii


def generate_keypair():
    sk = SigningKey.generate(curve=SECP256k1)
    vk = sk.get_verifying_key()
    priv_hex = sk.to_string().hex()
    pub_hex = vk.to_string().hex()
    return priv_hex, pub_hex


def sign_message(private_key_hex: str, message: str) -> str:
    try:
        sk = SigningKey.from_string(bytes.fromhex(private_key_hex), curve=SECP256k1)
    except Exception as e:
        raise ValueError("Invalid private key hex")
    msg = message.encode("utf-8")
    sig = sk.sign(msg)
    return sig.hex()


def verify_signature(public_key_hex: str, message: str, signature_hex: str) -> bool:
    try:
        vk = VerifyingKey.from_string(bytes.fromhex(public_key_hex), curve=SECP256k1)
        sig = bytes.fromhex(signature_hex)
        return vk.verify(sig, message.encode("utf-8"))
    except (BadSignatureError, Exception):
        return False


def pubkey_to_address(public_key_hex: str) -> str:
    # Simplified address: SHA256(pubkey) then hex-prefix
    h = hashlib.sha256(bytes.fromhex(public_key_hex)).hexdigest()
    return "0x" + h[:40]
