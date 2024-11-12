from typing import Optional
from user import User
from database import users_db
from password import hash_password_with_salt, verify_password_with_salt, validate_password

def register_user(username: str, email: str, password: str) -> bool:
    if not validate_password(password):
        raise ValueError("Password must be at least 8 characters long, include at least one digit, one uppercase letter, and one special character.")

    if username in users_db:
        return  False

    hashed_pw: str = hash_password_with_salt(password)
    new_user: User = User(username, email, hashed_pw)
    users_db[username] = new_user.to_dict()
    return True

def login_user(username: str, password: str) -> Optional[User]:
    user_data: str = users_db.get(username)
    if not user_data:
        return None
    if verify_password_with_salt(password, user_data["password"]):
        return User.from_dict(user_data)
    return None