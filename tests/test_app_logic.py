from app_logic.bmi import bmi_category, calculate_bmi
from app_logic.grades import calculate_grade
from app_logic.todo import create_task, delete_task, format_task, mark_completed
from app_logic.units import celsius_to_kelvin, convert_currency, convert_length, kelvin_to_celsius


def test_calculate_bmi_and_category():
    bmi = calculate_bmi(70, 1.75)
    assert round(bmi, 2) == 22.86
    assert bmi_category(bmi) == "Normal weight"


def test_calculate_grade():
    assert calculate_grade(95) == "A+"
    assert calculate_grade(41) == "D"
    assert calculate_grade(20) == "F"


def test_temperature_conversions():
    assert round(celsius_to_kelvin(0), 2) == 273.15
    assert round(kelvin_to_celsius(273.15), 2) == 0


def test_currency_and_length_conversions():
    assert round(convert_currency(10, "USD", "EUR"), 2) == 9.1
    assert round(convert_length(1, "km", "m"), 2) == 1000.0


def test_todo_helpers():
    tasks = [create_task("Read book")]
    mark_completed(tasks, 0)
    assert tasks[0]["completed"] is True
    assert format_task(tasks[0], 1) == "1. [✓] Read book"
    removed = delete_task(tasks, 0)
    assert removed["description"] == "Read book"
    assert tasks == []
