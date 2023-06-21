def celsius_to_fahrenheit(celsius):
    return (celsius * (9 / 5)) + 32

def check_temperature_validity(temperature, unit):
    abs_zero = {"C": -273.15,
                "F": -459.67,
                "K": 0}
    if temperature < abs_zero[unit]:
        return False
    return True

def check_unit_validity(unit):
    if not unit in ["C", "F", "K"]:
        return False
    return True

def convert_temperature(temperature, unit):
    if not check_unit_validity(unit):
        return "Invalid unit"
    if not check_temperature_validity(temperature, unit):
        return "Invalid temperature"
    if unit == "F":
        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) * (5 / 9)
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        fahrenheit = celsius_to_fahrenheit(celsius)
        return celsius, kelvin
    elif unit == "C":
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(temperature)
        # Convert Celsius to Kelvin
        kelvin = temperature + 273.15
        return fahrenheit, kelvin
    elif unit == "K":
        # Convert Kelvin to Celsius
        celsius = temperature - 273.15
        # Convert Celsius to Fahrenheit
        fahrenheit = celsius_to_fahrenheit(celsius)
        return celsius, fahrenheit


if __name__ == "__main__":
    print(convert_temperature(0, "C"))
    print(convert_temperature(0, "F"))
    print(convert_temperature(0, "K"))
    print(convert_temperature(-500, "K"))
    print(convert_temperature(-500, "C"))
    print(convert_temperature(-500, "F"))
    print(convert_temperature(0, "X"))
