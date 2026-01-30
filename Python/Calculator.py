while True:
    print("\n----- Calculator Menu ------")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exist")

    choice = input("Enter your choice: ")

    if choice == "5":
        print("Calculator closed")
        break

    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    match choice:
        case "1":
            print("Result = ", a+b)

        case "2":
            print("Result = ", a-b)

        case "3":
            print("Result = ", a*b)

        case "4":
            if b != 0:
                print("Result = ", a/b)
            else:
                print("Cannot divide by zero")

        case _:
            print("Invalid choice")

