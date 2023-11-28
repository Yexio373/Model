def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius
def convert_temperature(temperature, unit):
    if unit == "C":
        return celsius_to_fahrenheit(temperature)
    elif unit == "F":
        return fahrenheit_to_celsius(temperature)
    else:
        return "Invalid unit. Please enter either 'C' or 'F'."

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) / 1.8
    return celsius