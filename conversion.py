def celsius_to_fahrenheit(celsius):
    """Celsius to Fahrenheit conversion

    Args:
        celsius (float): temperature in degrees celsius

    Returns:
        float: temperature in degrees fahrenheit
    """
    return celsius/5*9 + 32

def celsius_to_kelvin(celsius):
    """Celsius to Kelvin conversion

    Args:
        celsius (float): temperature in degrees celsius

    Returns:
        float: temperature in degrees Kelvin
    """
    return celsius + 273.15

def kelvin_to_fahrenheit(kelvin):
    """Kelvin to Fahrenheit conversion

    Args:
        kelvin (float): temperature in degrees Kelvin

    Returns:
        float: temperature in degrees Fahrenheit
    """
    celsius = kelvin - 273.15
    return celsius_to_fahrenheit(celsius)