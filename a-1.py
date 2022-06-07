import os
import pickle

users = {}
if os.path.exists("users"):
    with open("users", "rb") as f:
        users = pickle.load(f)

def update():
    with open("users", "wb") as f:
        pickle.dump(users, f)

def sign_up():
    username = input("Enter username: ")
    password1 = input("Enter password: ")
    password2 = input("Re-enter password: ")
    if password1 != password2:
        print("Passwords do not match")
        sign_up()
    else:
        users[username] = password1
    update()

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("login successful")
    else:
        print("User does not exist")
        login()
        
if __name__ == "__main__":
    while True:
        print("1: Sign up")
        print("2: Login")
        choice = input()
        if choice == "1":
            sign_up()
        else:
            login()
            
