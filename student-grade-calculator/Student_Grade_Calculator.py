from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app_logic.grades import calculate_grade


def read_marks():
    while True:
        raw_value = input("Enter the marks (0-100): ").strip()
        try:
            return float(raw_value)
        except ValueError:
            print("Error: Please enter a valid number.")


def ask_to_continue():
    while True:
        answer = input("Do you want to calculate another grade? (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Please enter 'y' for yes or 'n' for no.")


def main():
    print("Student Grade Calculator")
    while True:
        try:
            marks = read_marks()
            grade = calculate_grade(marks)
        except ValueError as error:
            print(f"Error: {error}")
            continue

        print(f"Marks: {marks}")
        print(f"Grade: {grade}")

        if not ask_to_continue():
            print("Thank you for using the Student Grade Calculator!")
            break


if __name__ == "__main__":
    main()
