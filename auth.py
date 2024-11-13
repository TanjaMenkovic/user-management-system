from typing import Optional, Dict
from user import User
from database import add_user, get_user
from password import hash_password_with_salt, verify_password_with_salt, validate_password

def register_user(username: str, email: str, password: str) -> bool:
    """
    Registers a new user in the database.
    :param username: The unique username for the user.
    :param email: The user's email address.
    :param password: The plaintext password provided by the user.
    :return: True if the registration is successful, False if the username is already taken.
    """
    if not validate_password(password):
        raise ValueError(
            "Password must be at least 8 characters long, include at least one digit, "
            "one uppercase letter, and one special character."
        )
    hashed_pw_data: Dict[str, str] = hash_password_with_salt(password)
    return add_user(username, email, hashed_pw_data)

def login_user(username: str, password: str) -> Optional[User]:
    """
    Authenticates a user by verifying their password.
    :param username: The username of the user.
    :param password: The plaintext password provided by the user.
    :return: A User object if authentication is successful, None otherwise.
    """
    user_data: Optional[Dict[str, str]] = get_user(username)
    if not user_data:
        return None  # User not found

    hashed_pw_data: Dict[str, str] = {
        "hash": user_data["password_hash"],
        "salt": user_data["password_salt"],
    }
    if verify_password_with_salt(password, hashed_pw_data):
        return User.from_dict(user_data)
    return None
