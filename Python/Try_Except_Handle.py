try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a/b
    print("Result = ", result)

except ZeroDivisionError:
    print("Error: Cannot divided by zero")

except ValueError:
    print("Error: Please enter only numbers")

except Exception as e:
    print("Something went wrong:", e)

else:
    print("Program executed successfully")

finally:
    print("Program ended")