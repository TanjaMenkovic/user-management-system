from typing import Optional, Dict

class User:
    def __init__(self, username: str, email: str, password: Dict[str, str]) -> None:
        """
        Initializes a User object.
        :param username: The unique username for the user.
        :param email: The user's email address.
        :param password: A dictionary containing the hashed password and salt.
        """
        self.username: str = username
        self.email: str = email
        self.password: Dict[str, str] = password

    def to_dict(self) -> Dict[str, str]:
        """
        Converts the User object to a dictionary for storage.
        :return: A dictionary representation of the User.
        """
        return {
            "username": self.username,
            "email": self.email,
            "password_hash": self.password["hash"],
            "password_salt": self.password["salt"],
        }

    @staticmethod
    def from_dict(data: Dict[str, str]) -> Optional["User"]:
        """
        Creates a User object from a dictionary.
        :param data: The dictionary containing user data.
        :return: A User object if the dictionary contains the required fields, None otherwise.
        """
        if all(key in data for key in ("username", "email", "password_hash", "password_salt")):
            return User(
                username=data["username"],
                email=data["email"],
                password={"hash": data["password_hash"], "salt": data["password_salt"]},
            )
        return None
