def celsius_to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f

celsius = float(input("Enter tenperature in celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)

print("Temperature in Fahrenheit: ", fahrenheit)

