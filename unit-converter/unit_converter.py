def read_number(prompt):
    while True:
        raw_value = input(prompt).strip()
        if not raw_value:
            print("Please enter a value.")
            continue
        try:
            return float(raw_value)
        except ValueError:
            print("Please enter a valid number.")


def read_choice(prompt, valid_choices):
    while True:
        choice = input(prompt).strip()
        if choice in valid_choices:
            return choice
        print(f"Invalid choice! Please select one of: {', '.join(valid_choices)}.")


def temperature_converter():
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    choice = read_choice("Choose conversion (1-4): ", {"1", "2", "3", "4"})

    if choice == "1":
        celsius = read_number("Enter temperature in Celsius: ")
        print(f"{celsius}°C = {(celsius * 9 / 5) + 32}°F")
    elif choice == "2":
        fahrenheit = read_number("Enter temperature in Fahrenheit: ")
        print(f"{fahrenheit}°F = {(fahrenheit - 32) * 5 / 9}°C")
    elif choice == "3":
        celsius = read_number("Enter temperature in Celsius: ")
        kelvin = celsius + 273.15
        if kelvin < 0:
            print("That value would produce an invalid Kelvin temperature.")
            return
        print(f"{celsius}°C = {kelvin}K")
    else:
        kelvin = read_number("Enter temperature in Kelvin: ")
        if kelvin < 0:
            print("Kelvin cannot be negative.")
            return
        print(f"{kelvin}K = {kelvin - 273.15}°C")


def currency_converter():
    rates = {"USD": 1.0, "EUR": 0.91, "GBP": 0.78, "INR": 82.0}
    from_currency = input("From currency (USD, EUR, GBP, INR): ").strip().upper()
    to_currency = input("To currency (USD, EUR, GBP, INR): ").strip().upper()

    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency!")
        return

    amount = read_number(f"Amount in {from_currency}: ")
    converted = amount / rates[from_currency] * rates[to_currency]
    print(f"{amount} {from_currency} = {converted} {to_currency}")


def length_converter():
    print("\nLength Converter")
    print("Supported units: meter (m), kilometer (km), mile (mi), yard (yd), foot (ft)")
    units = {
        "m": 1.0,
        "km": 1000.0,
        "mi": 1609.34,
        "yd": 0.9144,
        "ft": 0.3048,
    }

    from_unit = input("From unit (m, km, mi, yd, ft): ").strip().lower()
    to_unit = input("To unit (m, km, mi, yd, ft): ").strip().lower()

    if from_unit not in units or to_unit not in units:
        print("Unsupported unit!")
        return

    length = read_number(f"Enter length in {from_unit}: ")
    length_in_meters = length * units[from_unit]
    print(f"{length} {from_unit} = {length_in_meters / units[to_unit]} {to_unit}")


def main():
    while True:
        print("\nUnit Converter")
        print("1. Temperature")
        print("2. Currency")
        print("3. Length")
        print("4. Exit")
        choice = read_choice("Choose conversion type (1-4): ", {"1", "2", "3", "4"})

        if choice == "1":
            temperature_converter()
        elif choice == "2":
            currency_converter()
        elif choice == "3":
            length_converter()
        else:
            print("Exiting... Goodbye!")
            break


if __name__ == "__main__":
    main()
