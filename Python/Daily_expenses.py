def add_expense():
    date = input("Enter date (DD-MM-YYYY): ")
    item = input("Enter expense name: ")
    amount = input("Enter amount: ")

    with open("expenses.txt", "a") as file:
        file.write(f"{date} | {item} | {amount}\n")
    
    print("Expense added successfully!")

def view_expense():
    print("\n---- All Expenses ----")
    try:
        with open("expenses.txt","r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No expenses found!")


while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expense()
    elif choice == "3":
        print("Exiting Expense Tracker")
        break
    else:
        print("Invalid choice, try again")