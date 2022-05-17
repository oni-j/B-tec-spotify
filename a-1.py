def check():
    if stored_username == username and stored_password == password:
        print("Welcome back")

def login():
    stored_username = input("Please enter your username")
    stored_password = input("Please enetr your password")
    check()

def signup():
    temp_username = input("Please enter a username")
    while temp_username in username_data:
        print("That username is already in use")
    username_data.append(temp_username)
    temp_password = input("Please enter a password")
    if temp_password == temp_password.lower():
        print("Please include an uppercase letter")
    elif len(temp_password) <= 6:
        print("Please make your password longer than 6 letters")
user_data{'username': stored_username, 'stored_password': stored_password}


