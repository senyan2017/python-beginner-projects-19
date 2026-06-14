from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app_logic.bmi import bmi_category, calculate_bmi


def main():
    print("BMI Calculator")
    try:
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
    except ValueError as error:
        print(error)
        return

    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {bmi_category(bmi)}")


if __name__ == "__main__":
    main()
