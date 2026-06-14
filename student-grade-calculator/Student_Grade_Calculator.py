def calculate_grade(marks):
    if 90 <= marks <= 100:
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
    if marks >= 0:
        return "F"
    return None


def main():
    print("Student Grade Calculator")
    while True:
        while True:
            raw_marks = input("Enter the marks (0-100): ").strip()
            try:
                marks = float(raw_marks)
            except ValueError:
                print("Error: Please enter a valid number.")
                continue
            if marks < 0 or marks > 100:
                print("Error: Marks should be between 0 and 100.")
                continue
            break

        grade = calculate_grade(marks)
        print(f"Marks: {marks}")
        print(f"Grade: {grade}")

        again = input("Do you want to calculate another grade? (y/n): ").strip().lower()
        if again == "y":
            continue
        if again == "n":
            print("Thank you for using the Student Grade Calculator!")
            break
        print("Please enter 'y' for yes or 'n' for no.")
        while again not in {"y", "n"}:
            again = input("Do you want to calculate another grade? (y/n): ").strip().lower()
            if again == "y":
                break
            if again == "n":
                print("Thank you for using the Student Grade Calculator!")
                return
            print("Please enter 'y' for yes or 'n' for no.")
        if again == "y":
            continue
        return


if __name__ == "__main__":
    main()
