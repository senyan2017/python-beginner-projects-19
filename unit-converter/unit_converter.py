from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from shared_logic.unit_tools import (
    CURRENCY_RATES,
    TEMPERATURE_CHOICES,
    UNITS_IN_METERS,
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    convert_currency,
    convert_length,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def read_number(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Please enter a valid number.")
        return None


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose conversion (1-4): ").strip()

    if choice not in TEMPERATURE_CHOICES:
        print("Invalid choice!")
        return

    if choice == "1":
        value = read_number("Enter temperature in Celsius: ")
        if value is not None:
            print(f"{value}°C = {celsius_to_fahrenheit(value)}°F")
    elif choice == "2":
        value = read_number("Enter temperature in Fahrenheit: ")
        if value is not None:
            print(f"{value}°F = {fahrenheit_to_celsius(value)}°C")
    elif choice == "3":
        value = read_number("Enter temperature in Celsius: ")
        if value is not None:
            print(f"{value}°C = {celsius_to_kelvin(value)}K")
    else:
        value = read_number("Enter temperature in Kelvin: ")
        if value is not None:
            print(f"{value}K = {kelvin_to_celsius(value)}°C")


def currency_converter():
    from_currency = input("From currency (USD, EUR, GBP, INR): ").upper()
    to_currency = input("To currency (USD, EUR, GBP, INR): ").upper()

    if from_currency not in CURRENCY_RATES or to_currency not in CURRENCY_RATES:
        print("Unsupported currency!")
        return

    amount = read_number(f"Amount in {from_currency}: ")
    if amount is None:
        return
    print(f"{amount} {from_currency} = {convert_currency(amount, from_currency, to_currency)} {to_currency}")


def length_converter():
    print("\nLength Converter")
    print("Supported units: meter (m), kilometer (km), mile (mi), yard (yd), foot (ft)")
    from_unit = input("From unit (m, km, mi, yd, ft): ").lower()
    to_unit = input("To unit (m, km, mi, yd, ft): ").lower()

    if from_unit not in UNITS_IN_METERS or to_unit not in UNITS_IN_METERS:
        print("Unsupported unit!")
        return

    length = read_number(f"Enter length in {from_unit}: ")
    if length is None:
        return
    print(f"{length} {from_unit} = {convert_length(length, from_unit, to_unit)} {to_unit}")


def main():
    while True:
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Currency")
        print("3. Length")
        print("4. Exit")
        choice = input("Choose conversion type (1-4): ").strip()

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            length_converter()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1-4.")


if __name__ == "__main__":
    main()
