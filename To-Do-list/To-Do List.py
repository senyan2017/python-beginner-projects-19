from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parents[1]))

from shared_logic.todo_tools import add_task as add_task_item
from shared_logic.todo_tools import complete_task, delete_task as delete_task_item, format_task


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
    if add_task_item(tasks, description):
        print("Task added.")
    else:
        print("Empty task description not added.")


def mark_completed(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    try:
        number = int(input("Enter task number to mark as completed: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    if complete_task(tasks, number - 1):
        print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    try:
        number = int(input("Enter task number to delete: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    removed = delete_task_item(tasks, number - 1)
    if removed is None:
        print("Invalid task number.")
    else:
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
            mark_completed(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
