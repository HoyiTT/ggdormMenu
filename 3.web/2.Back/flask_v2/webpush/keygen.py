from pywebpush import WebPusher, WebPushException
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend

def generate_vapid_keys():
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    # 개인 키를 PEM 형식으로 직렬화
    pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    # 공개 키를 PEM 형식으로 직렬화
    public_key = private_key.public_key()
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return pem.decode('utf-8'), public_pem.decode('utf-8')

private_key, public_key = generate_vapid_keys()
print("Private Key:", private_key)
print("Public Key:", public_key)
