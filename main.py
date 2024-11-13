from auth import register_user, login_user
from database import initialize_database

def main() -> None:
    initialize_database()  # Set up the database
    print("Welcome to the User Management System")
    while True:
        print("\nChoose an option:")
        print(" 1. Register")
        print(" 2. Login")
        print(" 3. Exit")
        choice: str = input("Enter your choice: ")

        if choice == "1":
            username: str = input("Enter a username: ")
            email: str = input("Enter an email: ")
            password: str = input("Enter a password: ")
            try:
                if register_user(username, email, password):
                    print("\nRegistration successful!")
                else:
                    print("\nUsername already taken. Please try again.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == "2":
            username: str = input("Enter your username: ")
            password: str = input("Enter your password: ")
            user = login_user(username, password)
            if user:
                print(f"\nWelcome back, {user.username}!")
                print(f"Your email: {user.email}")
            else:
                print("\nInvalid credentials. Please try again.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
