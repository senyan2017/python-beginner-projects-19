def create_task(description):
    clean_description = description.strip()
    if not clean_description:
        raise ValueError("Task description cannot be empty.")
    return {"description": clean_description, "completed": False}


def format_task(task, index):
    status = "✓" if task["completed"] else "✗"
    return f"{index}. [{status}] {task['description']}"


def mark_completed(tasks, index):
    if not 0 <= index < len(tasks):
        raise IndexError("Invalid task number.")
    tasks[index]["completed"] = True


def delete_task(tasks, index):
    if not 0 <= index < len(tasks):
        raise IndexError("Invalid task number.")
    return tasks.pop(index)
