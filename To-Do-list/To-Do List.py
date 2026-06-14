import json
import os
import sys
import tempfile

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks(data_file=DATA_FILE):
    if not os.path.exists(data_file):
        return []
    try:
        with open(data_file, "r", encoding="utf-8") as file:
            data = json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Warning: task data could not be read. Starting with an empty list.")
        return []
    if not isinstance(data, list):
        print("Warning: task data is invalid. Starting with an empty list.")
        return []

    tasks = []
    for item in data:
        if not isinstance(item, dict):
            continue
        description = str(item.get("description", "")).strip()
        if not description:
            continue
        tasks.append({
            "description": description,
            "completed": bool(item.get("completed", False)),
        })
    return tasks


def save_tasks(tasks, data_file=DATA_FILE):
    try:
        with open(data_file, "w", encoding="utf-8") as file:
            json.dump(tasks, file, ensure_ascii=False, indent=2)
    except OSError:
        print("Warning: failed to save tasks.")


def display_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Edit task")
    print("5. Delete task")
    print("6. Exit")


def view_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
        return
    print("\nTasks:")
    for index, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{index}. [{status}] {task['description']}")


def prompt_index(tasks, message):
    if not tasks:
        print("No tasks available.")
        return None
    raw = input(message).strip()
    if not raw:
        print("Please enter a task number.")
        return None
    try:
        index = int(raw)
    except ValueError:
        print("Please enter a valid number.")
        return None
    if not 1 <= index <= len(tasks):
        print("Invalid task number.")
        return None
    return index - 1


def add_task(tasks, data_file=DATA_FILE):
    description = input("Enter task description: ").strip()
    if not description:
        print("Empty task description not added.")
        return
    tasks.append({"description": description, "completed": False})
    save_tasks(tasks, data_file)
    print("Task added.")


def mark_completed(tasks, data_file=DATA_FILE):
    index = prompt_index(tasks, "Enter task number to mark as completed: ")
    if index is None:
        return
    if tasks[index]["completed"]:
        print("Task is already completed.")
        return
    tasks[index]["completed"] = True
    save_tasks(tasks, data_file)
    print("Task marked as completed.")


def edit_task(tasks, data_file=DATA_FILE):
    index = prompt_index(tasks, "Enter task number to edit: ")
    if index is None:
        return
    description = input("Enter new task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return
    tasks[index]["description"] = description
    save_tasks(tasks, data_file)
    print("Task updated.")


def delete_task(tasks, data_file=DATA_FILE):
    index = prompt_index(tasks, "Enter task number to delete: ")
    if index is None:
        return
    removed = tasks.pop(index)
    save_tasks(tasks, data_file)
    print(f"Deleted task: {removed['description']}")


def run_self_test():
    with tempfile.TemporaryDirectory() as temp_dir:
        data_file = os.path.join(temp_dir, "tasks.json")
        tasks = []
        tasks.append({"description": "alpha", "completed": False})
        save_tasks(tasks, data_file)
        loaded = load_tasks(data_file)
        if len(loaded) != 1 or loaded[0]["description"] != "alpha":
            print("SELF-TEST FAILED: save/load")
            return 1
        loaded[0]["completed"] = True
        save_tasks(loaded, data_file)
        reloaded = load_tasks(data_file)
        if not reloaded[0]["completed"]:
            print("SELF-TEST FAILED: completion persistence")
            return 1
        reloaded[0]["description"] = "beta"
        save_tasks(reloaded, data_file)
        final_tasks = load_tasks(data_file)
        if final_tasks[0]["description"] != "beta":
            print("SELF-TEST FAILED: edit persistence")
            return 1
        final_tasks.pop()
        save_tasks(final_tasks, data_file)
        if load_tasks(data_file):
            print("SELF-TEST FAILED: delete persistence")
            return 1
    print("SELF-TEST PASSED")
    return 0


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--self-test":
        raise SystemExit(run_self_test())

    tasks = load_tasks()
    if tasks:
        print(f"Loaded {len(tasks)} task(s).")

    while True:
        display_menu()
        choice = input("Choose an option: ").strip()
        if not choice:
            print("Please enter a menu number.")
            continue
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_completed(tasks)
        elif choice == "4":
            edit_task(tasks)
        elif choice == "5":
            delete_task(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
