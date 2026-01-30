email = input("Emter email: ")
password = input("Enter password: ")

if '@' in email and '.' in email:
    print("Email is valid")
else:
    print("Email is not valid")

if len(password) >= 6:
    print("Password is valid")
else:
    print("Password is too short")