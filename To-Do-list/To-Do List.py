from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app_logic.todo import create_task, delete_task, format_task, mark_completed


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("\nTasks:")
    for index, task in enumerate(tasks, 1):
        print(format_task(task, index))


def add_task(tasks):
    description = input("Enter task description: ").strip()
    try:
        tasks.append(create_task(description))
    except ValueError as error:
        print(error)
        return
    print("Task added.")


def complete_task(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    try:
        number = int(input("Enter task number to mark as completed: "))
        mark_completed(tasks, number - 1)
    except ValueError:
        print("Please enter a valid number.")
        return
    except IndexError as error:
        print(error)
        return
    print("Task marked as completed.")


def remove_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        number = int(input("Enter task number to delete: "))
        removed = delete_task(tasks, number - 1)
    except ValueError:
        print("Please enter a valid number.")
        return
    except IndexError as error:
        print(error)
        return
    print(f"Deleted task: {removed['description']}")


def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
