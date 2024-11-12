from typing import Optional, Dict

class User:
    def __init__(self, username: str, email: str, password: Dict[str, str]) -> None:
        self.username: str = username
        self.email: str = email
        self.password: Dict[str, str] = password

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "email": self.email,
            "password": self.password
        }

    @staticmethod
    def from_dict(data: dict) -> Optional['User']:
        if all(key in data for key in ("username", "email", "password")):
            return User(data["username"], data["email"], data["password"])
        return None