from masterlistTest import changeformat
from masterlistTest import addsong
from songClass import Song
from masterlistTest import masterlist
import os
import pickle

def viewMasterlist():
    print(masterlist)
    for song in masterlist:
        print(song.name, song.length)

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
        loginOptions()
    update()

#Login function which checks whether the entered password matches the password linked to the username
def login():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in users and users[username] == password:
        print("login successful")
        loggedIn = True
    else:
        print("User does not exist")
        loginOptions()

def loginOptions():
    print("1: Sign up")
    print("2: Login")
    choice = input()
    if choice == "1":
        sign_up()
    elif choice == "2":
        login()
    else:
        print("please enter a 1 or a 2")
        loginOptions()
    
loginOptions()

while True:
    tempCmd = int(input("What would you like to do? \n 1. add to masterlist \n 2. view masterlist \n")) - 1
    cmdList = ("addsong", "viewMasterlist")
    if tempCmd in (1, 2):
        funcName = cmdList[tempCmd]
        locals()[funcName]()
    else:
        print("Please choose a valid option")
