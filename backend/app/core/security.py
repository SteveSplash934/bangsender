from cryptography.fernet import Fernet
from app.core.config import settings
import base64

# We need a 32-byte key. 
# In production, this should be loaded strictly from env vars.
# For now, we derive it or use a generated one.

def get_cipher_suite():
    # Ensure SECRET_KEY is proper length for Fernet (32 url-safe base64-encoded bytes)
    # This is a quick hack to make any string work as a key
    key = settings.SECRET_KEY
    if len(key) < 32:
        # Pad if too short
        key = key.ljust(32, '0')
    elif len(key) > 32:
        # Truncate if too long
        key = key[:32]
        
    # Fernet requires a base64 encoded 32-byte key
    # We'll just encode our key to satisfy the requirement
    encoded_key = base64.urlsafe_b64encode(key.encode())
    return Fernet(encoded_key)

def encrypt_password(password: str) -> str:
    cipher = get_cipher_suite()
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(encrypted_password: str) -> str:
    cipher = get_cipher_suite()
    return cipher.decrypt(encrypted_password.encode()).decode()