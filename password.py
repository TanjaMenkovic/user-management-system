import hashlib
import os
import re
from typing import Dict

def hash_password_with_salt(password: str) -> Dict[str, str]:
    salt: bytes = os.urandom(16)
    hashed_password: bytes = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return {"salt": salt.hex(), "hash": hashed_password.hex()}

def verify_password_with_salt(password: str, hashed_data: Dict[str, str]) -> bool:
    salt: bytes = bytes.fromhex(hashed_data["salt"])
    hashed_password: bytes = hashlib.pbkdf2_hmac("sha256", password.encode(), salt, 100000)
    return hashed_password.hex() == hashed_data["hash"]

def validate_password(password: str) -> bool:
    """
    Validates a password to ensure it meets the following criteria:
    - At least 8 characters long.
    - Contains at least one digit.
    - Contains at least one uppercase letter.
    - Contains at least one special character (non-alphanumeric).
    Returns True if the password meets the criteria, False otherwise.
    """
    if len(password) < 8 or not any(c.isdigit() for c in password):
        return False
    if not any(c.isupper() for c in password) or not re.search(r"[^\w\s]", password):
        return False
    return True
