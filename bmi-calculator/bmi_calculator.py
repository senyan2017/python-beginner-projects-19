from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from shared_logic.bmi_tools import bmi_category, calculate_bmi


def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Please enter valid numeric values.")
        return

    if weight <= 0 or height <= 0:
        print("Weight and height must be positive numbers.")
        return

    bmi = calculate_bmi(weight, height)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {bmi_category(bmi)}")


if __name__ == "__main__":
    main()
