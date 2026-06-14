def read_number(prompt):
    raw_value = input(prompt).strip()
    try:
        return float(raw_value)
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

    if choice == "1":
        celsius = read_number("Enter temperature in Celsius: ")
        if celsius is None:
            return
        fahrenheit = (celsius * 9 / 5) + 32
        print(f"{celsius}°C = {fahrenheit}°F")
    elif choice == "2":
        fahrenheit = read_number("Enter temperature in Fahrenheit: ")
        if fahrenheit is None:
            return
        celsius = (fahrenheit - 32) * 5 / 9
        print(f"{fahrenheit}°F = {celsius}°C")
    elif choice == "3":
        celsius = read_number("Enter temperature in Celsius: ")
        if celsius is None:
            return
        kelvin = celsius + 273.15
        print(f"{celsius}°C = {kelvin}K")
    elif choice == "4":
        kelvin = read_number("Enter temperature in Kelvin: ")
        if kelvin is None:
            return
        if kelvin < 0:
            print("Kelvin cannot be negative.")
            return
        celsius = kelvin - 273.15
        print(f"{kelvin}K = {celsius}°C")
    else:
        print("Invalid choice!")


def currency_converter():
    rates = {"USD": 1.0, "EUR": 0.91, "GBP": 0.78, "INR": 82.0}
    from_currency = input("From currency (USD, EUR, GBP, INR): ").strip().upper()
    to_currency = input("To currency (USD, EUR, GBP, INR): ").strip().upper()

    if from_currency not in rates or to_currency not in rates:
        print("Unsupported currency!")
        return

    amount = read_number(f"Amount in {from_currency}: ")
    if amount is None:
        return
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
    if length is None:
        return

    length_in_meters = length * units[from_unit]
    converted_length = length_in_meters / units[to_unit]
    print(f"{length} {from_unit} = {converted_length} {to_unit}")


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
