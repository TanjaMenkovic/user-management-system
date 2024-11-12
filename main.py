from auth import register_user, login_user

def main() -> None:
    print("Welcome to the User Management System:")
    while True:
        print("\nChoose an option:\n      1. Register\n      2. Login\n      3. Exit\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter a username: ")
            email = input("Enter an email: ")
            password = input("Enter a password: ")
            try:
                if register_user(username, email, password):
                    print("\nRegistration successful!")
                else:
                 print("\nUsername already taken. Please try again.")
            except ValueError as e:
                print(f"\nError: {e}")

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            user = login_user(username, password)
            if user:
                print(f"\nWelcome back, {user.username}!\nYour email: {user.email}")
            else:
                print("\nInvalid credentials. Please try again.")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
