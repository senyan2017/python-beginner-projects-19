def calculate_grade(marks):
    if not 0 <= marks <= 100:
        raise ValueError("Marks should be between 0 and 100.")
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
