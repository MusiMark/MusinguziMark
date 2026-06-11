username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

username = "resses2026"
password = "password123"

if username_input == username: 
    if password_input == password:
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Invalid username.")
