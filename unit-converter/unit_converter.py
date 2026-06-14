from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app_logic.units import (
    CURRENCY_RATES,
    LENGTH_FACTORS,
    celsius_to_fahrenheit,
    celsius_to_kelvin,
    convert_currency,
    convert_length,
    fahrenheit_to_celsius,
    kelvin_to_celsius,
)


def read_number(prompt):
    while True:
        raw_value = input(prompt).strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number.")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = input("Choose conversion (1-4): ").strip()

    try:
        if choice == "1":
            value = read_number("Enter temperature in Celsius: ")
            print(f"{value}°C = {celsius_to_fahrenheit(value)}°F")
        elif choice == "2":
            value = read_number("Enter temperature in Fahrenheit: ")
            print(f"{value}°F = {fahrenheit_to_celsius(value)}°C")
        elif choice == "3":
            value = read_number("Enter temperature in Celsius: ")
            print(f"{value}°C = {celsius_to_kelvin(value)}K")
        elif choice == "4":
            value = read_number("Enter temperature in Kelvin: ")
            print(f"{value}K = {kelvin_to_celsius(value)}°C")
        else:
            print("Invalid choice!")
    except ValueError as error:
        print(error)


def currency_converter():
    from_currency = input("From currency (USD, EUR, GBP, INR): ").strip().upper()
    to_currency = input("To currency (USD, EUR, GBP, INR): ").strip().upper()
    amount = read_number(f"Amount in {from_currency}: ")
    try:
        converted = convert_currency(amount, from_currency, to_currency)
    except ValueError as error:
        print(error)
        return
    print(f"{amount} {from_currency} = {converted} {to_currency}")


def length_converter():
    print("\nLength Converter")
    print("Supported units: meter (m), kilometer (km), mile (mi), yard (yd), foot (ft)")
    from_unit = input("From unit (m, km, mi, yd, ft): ").strip().lower()
    to_unit = input("To unit (m, km, mi, yd, ft): ").strip().lower()
    length = read_number(f"Enter length in {from_unit}: ")
    try:
        converted = convert_length(length, from_unit, to_unit)
    except ValueError as error:
        print(error)
        return
    print(f"{length} {from_unit} = {converted} {to_unit}")


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
