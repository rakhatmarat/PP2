def fahrenheit_to_celsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

fahrenheit = float(input("Enter the temperature in Fahrenheit: "))

celsius = fahrenheit_to_celsius(fahrenheit)

print("Equivalent temperature in Celsius:", celsius)
