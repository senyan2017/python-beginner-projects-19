import json
import os

DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tasks.json")


def load_tasks():
    """Load tasks from the JSON file. Returns an empty list if the file is
    missing, unreadable, or contains invalid data (with a warning printed)."""
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError) as e:
        print(f"Warning: could not read {DATA_FILE} ({e}). Starting with an empty task list.")
        return []

    if not isinstance(data, list):
        print("Warning: tasks file did not contain a list. Starting with an empty task list.")
        return []

    cleaned = []
    for item in data:
        if isinstance(item, dict) and "description" in item:
            cleaned.append({
                "description": str(item["description"]),
                "completed": bool(item.get("completed", False)),
            })
    if len(cleaned) != len(data):
        print("Warning: some entries in the task file were invalid and were skipped.")
    return cleaned


def save_tasks(tasks):
    """Persist the current task list to disk. Failures are reported but do not
    crash the program."""
    try:
        with open(DATA_FILE, "w", encoding="utf-8") as f:
            json.dump(tasks, f, ensure_ascii=False, indent=2)
    except OSError as e:
        print(f"Warning: failed to save tasks ({e}).")


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
    for idx, task in enumerate(tasks, 1):
        status = "✓" if task["completed"] else "✗"
        print(f"{idx}. [{status}] {task['description']}")


def add_task(tasks):
    desc = input("Enter task description: ").strip()
    if not desc:
        print("Empty task description not added.")
        return
    tasks.append({"description": desc, "completed": False})
    save_tasks(tasks)
    print("Task added.")


def mark_completed(tasks):
    if not tasks:
        print("No tasks to mark.")
        return
    raw = input("Enter task number to mark as completed: ").strip()
    if not raw:
        print("No input provided.")
        return
    try:
        num = int(raw)
    except ValueError:
        print("Please enter a valid number.")
        return
    if 1 <= num <= len(tasks):
        if tasks[num - 1]["completed"]:
            print("That task is already completed.")
        else:
            tasks[num - 1]["completed"] = True
            save_tasks(tasks)
            print("Task marked as completed.")
    else:
        print("Invalid task number.")


def delete_task(tasks):
    if not tasks:
        print("No tasks to delete.")
        return
    raw = input("Enter task number to delete: ").strip()
    if not raw:
        print("No input provided.")
        return
    try:
        num = int(raw)
    except ValueError:
        print("Please enter a valid number.")
        return
    if 1 <= num <= len(tasks):
        removed = tasks.pop(num - 1)
        save_tasks(tasks)
        print(f"Deleted task: {removed['description']}")
    else:
        print("Invalid task number.")


def main():
    tasks = load_tasks()
    if tasks:
        print(f"Loaded {len(tasks)} task(s) from {DATA_FILE}.")
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
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
