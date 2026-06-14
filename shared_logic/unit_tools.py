TEMPERATURE_CHOICES = {"1", "2", "3", "4"}

UNITS_IN_METERS = {
    "m": 1.0,
    "km": 1000.0,
    "mi": 1609.34,
    "yd": 0.9144,
    "ft": 0.3048,
}

CURRENCY_RATES = {"USD": 1.0, "EUR": 0.91, "GBP": 0.78, "INR": 82.0}


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def convert_currency(amount, from_currency, to_currency):
    return amount / CURRENCY_RATES[from_currency] * CURRENCY_RATES[to_currency]


def convert_length(length, from_unit, to_unit):
    return length * UNITS_IN_METERS[from_unit] / UNITS_IN_METERS[to_unit]
