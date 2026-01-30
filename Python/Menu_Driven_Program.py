while True:
    print("\n----MENU----")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Sum = ", a+b)

    elif choice == "2":
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Difference = ", a-b)

    elif choice == "3":
        print("Exiting Program....")
        break

    else:
        print("Invalid Choice, Try again")