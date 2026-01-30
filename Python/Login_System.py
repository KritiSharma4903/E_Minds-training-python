def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

    with open("user.txt", "a") as file:
        file.write(username + "," + password + "\n")

    print("Registration successful ✅")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("user.txt", "r") as file:
        for line in file:
            stored_user, stored_pass = line.strip().split(",")

            if username == stored_user and password == stored_pass:
                print("Login successful ✅")
                return

    print("Invalid username or password ❌")


# -------- MENU (Function ke bahar hona chahiye) --------
while True:
    print("\n-- MENU --")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Program ended")
        break
    else:
        print("Invalid choice")
