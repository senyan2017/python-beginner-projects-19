def calculate_bmi(weight, height):
    if weight <= 0 or height <= 0:
        raise ValueError("Weight and height must be positive numbers.")
    return weight / (height ** 2)


def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"
    return "Obesity"
