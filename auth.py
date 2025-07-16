from utils.auth_utils import *
from passwordChecker import password_check

DATA_FILE = "users.json"


def log_in():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    data = read_data()
    for user in data["users"]:
        if user["name"] == username and user["password"] == password:
            print(f"Login successful! welcome {username}!")
            set_current_user(username)
            return True
    print("Invalid username or password.")
    return False


def register():
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    pass_check = password_check(password)
    data = read_data()
    if pass_check > 7:
        new_user = {
            "id": len(data["users"]) + 1,
            "name": username,
            "password": password,
        }
        append_data(new_user)
        print("Registration successful! You can now log in.")
        return True
    else:
        print("Password is too weak..!!")
        return False
