import pytest
from conversion import celsius_to_fahrenheit

def test_celsius_to_fahrenheit():
    assert celsius_to_fahrenheit(20) == 68
    assert celsius_to_fahrenheit(30) == 86
    assert celsius_to_fahrenheit(0) == 32
    assert round(celsius_to_fahrenheit(9), 0) == 48
    assert abs(celsius_to_fahrenheit(9) - 48) < 0.21

def test_celsius_to_fahrenheit_invalid():
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("Invalid")

def test_celsius_to_fahrenheit_none():
    assert celsius_to_fahrenheit(None) is None

def test_that_doesnot_do_anything():
    celsius_to_fahrenheit(0)