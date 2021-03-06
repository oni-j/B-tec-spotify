import os
import pickle

users = {}
if os.path.exists("users"):
    with open("users", "rb") as f:
        users = pickle.load(f)

def update():
    with open("users", "wb") as f:
        pickle.dump(users, f)

#sign-up funtction which requires two passwords which both match to succesfully sign-up
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

#Login function which checks whether the entered password matches the password linked to the username
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
        elif choice == "2":
            login()
        else:
            print("Please input number 1 or 2.")

