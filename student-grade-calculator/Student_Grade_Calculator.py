from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from shared_logic.grade_tools import calculate_grade


def read_marks():
    while True:
        try:
            marks = float(input("Enter the marks (0-100): "))
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if calculate_grade(marks) is None:
            print("Error: Marks should be between 0 and 100.")
            continue
        return marks


def main():
    print("Student Grade Calculator")
    while True:
        marks = read_marks()
        print(f"Marks: {marks}")
        print(f"Grade: {calculate_grade(marks)}")
        again = input("Do you want to calculate another grade? (y/n): ").strip().lower()
        if again == "y":
            continue
        if again == "n":
            print("Thank you for using the Student Grade Calculator!")
            break
        print("Please enter 'y' for yes or 'n' for no.")


if __name__ == "__main__":
    main()
