CURRENCY_RATES = {"USD": 1.0, "EUR": 0.91, "GBP": 0.78, "INR": 82.0}
LENGTH_FACTORS = {
    "m": 1.0,
    "km": 1000.0,
    "mi": 1609.34,
    "yd": 0.9144,
    "ft": 0.3048,
}


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    if kelvin < 0:
        raise ValueError("That value would produce an invalid Kelvin temperature.")
    return kelvin


def kelvin_to_celsius(kelvin):
    if kelvin < 0:
        raise ValueError("Kelvin cannot be negative.")
    return kelvin - 273.15


def convert_currency(amount, from_currency, to_currency):
    if from_currency not in CURRENCY_RATES or to_currency not in CURRENCY_RATES:
        raise ValueError("Unsupported currency!")
    return amount / CURRENCY_RATES[from_currency] * CURRENCY_RATES[to_currency]


def convert_length(length, from_unit, to_unit):
    if from_unit not in LENGTH_FACTORS or to_unit not in LENGTH_FACTORS:
        raise ValueError("Unsupported unit!")
    return length * LENGTH_FACTORS[from_unit] / LENGTH_FACTORS[to_unit]
