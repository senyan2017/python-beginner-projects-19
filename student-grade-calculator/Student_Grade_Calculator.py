def calculate_grade(marks):
    if not 0 <= marks <= 100:
        return None
    if marks >= 90:
        return "A+"
    if marks >= 80:
        return "A"
    if marks >= 70:
        return "B+"
    if marks >= 60:
        return "B"
    if marks >= 50:
        return "C"
    if marks >= 40:
        return "D"
    return "F"


def read_marks():
    while True:
        raw_value = input("Enter the marks (0-100): ").strip()
        if not raw_value:
            print("Error: Please enter a value.")
            continue
        try:
            marks = float(raw_value)
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
        if not 0 <= marks <= 100:
            print("Error: Marks should be between 0 and 100.")
            continue
        return marks


def ask_to_continue():
    while True:
        answer = input("Do you want to calculate another grade? (y/n): ").strip().lower()
        if answer in {"y", "n"}:
            return answer == "y"
        print("Please enter 'y' for yes or 'n' for no.")


def main():
    print("Student Grade Calculator")
    while True:
        marks = read_marks()
        grade = calculate_grade(marks)
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")
        if not ask_to_continue():
            print("Thank you for using the Student Grade Calculator!")
            break


if __name__ == "__main__":
    main()
