import re
from sqlalchemy.orm import sessionmaker
from database_setup import engine, User

# Initialize the database session
Session = sessionmaker(bind=engine)
session = Session()

def display_menu(file_path):
    """Display menu from a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            print(file.read())
    except FileNotFoundError:
        print("Menu file not found. Please ensure the file exists.")

def validate_password(password):
    """Validate password based on specific rules."""
    if (len(password) >= 6 and len(password) <= 12 and
        re.match(r'^[!@#$%^&*]', password) and
        any(c.isdigit() for c in password) and
        any(c.islower() for c in password) and
        any(c.isupper() for c in password)):
        return True
    return False

def register_user():
    """Register a new user."""
    print("\n*** User Registration ***")
    while True:
        username = input("Enter a username: ")
        # Check if the username already exists in the database
        existing_user = session.query(User).filter_by(username=username).first()
        if existing_user:
            print("Username already exists. Try a different one.")
        else:
            break
    while True:
        password = input("Enter a password: ")
        if validate_password(password):
            # Add the new user to the database
            new_user = User(username=username, password=password)
            session.add(new_user)
            session.commit()
            print("Registration successful!")
            break
        else:
            print("Invalid password. Please follow the rules:")
            print("1. Starts with one of these: !@#$%^&*")
            print("2. Contains at least one digit, one uppercase, and one lowercase letter.")
            print("3. Length is between 6 and 12 characters.\n")

def login_user():
    """Login an existing user."""
    print("\n*** User Login ***")
    while True:
        username = input("Enter your username: ")
        # Check if the username exists in the database
        user = session.query(User).filter_by(username=username).first()
        if not user:
            print("Username does not exist. Please register first.")
            return
        else:
            break
    while True:
        password = input("Enter your password: ")
        if user.password == password:
            print(f"Welcome back, {username}!")
            break
        else:
            print("Incorrect password. Try again.")

def main():
    """Main function to run the program."""
    while True:
        # Display the main menu
        display_menu('welcome.txt')  # Ensure 'welcome.txt' is in the same directory
        choice = input("Select an option (1-3): ")
        if choice == '1':
            login_user()
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == '__main__':
    main()
