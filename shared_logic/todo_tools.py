def format_task(task, index):
    status = "✓" if task["completed"] else "✗"
    return f"{index}. [{status}] {task['description']}"


def add_task(tasks, description):
    description = description.strip()
    if not description:
        return False
    tasks.append({"description": description, "completed": False})
    return True


def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = True
        return True
    return False


def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        return tasks.pop(index)
    return None
