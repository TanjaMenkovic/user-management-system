# utils.py
import hashlib
import os
from typing import Dict

# def hash_password(password: str) -> str:
#     return hashlib.sha256(password.encode()).hexdigest()

# def verify_password(password: str, hashed_password: str) -> bool:
#     return hash_password(password) == hashed_password

def hash_password_with_salt(password: str) -> Dict[str, str]:
    salt = os.urandom(16)  # Generate a random 16-byte salt
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return {"salt": salt.hex(), "hash": hashed_password.hex()}

def verify_password_with_salt(password: str, hashed_data: Dict[str, str]) -> bool:
    salt = bytes.fromhex(hashed_data["salt"])
    hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
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
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    if not re.search(r"[^\w\s]", password):  # Match any non-alphanumeric character
        return False
    return True