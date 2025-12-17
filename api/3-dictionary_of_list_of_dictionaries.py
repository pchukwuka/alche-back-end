.
#!/usr/bin/python3
"""Export all employee TODOs to JSON file"""
import json
import requests


if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    # Get all users and all todos
    users = requests.get(users_url).json()
    todos = requests.get(todos_url).json()

    # Map user id to username
    user_names = {user["id"]: user["username"] for user in users}

    # Build the big dictionary
    all_tasks = {}

    for todo in todos:
        user_id = todo["userId"]
        user_id_str = str(user_id)

        task_info = {
            "username": user_names[user_id],
            "task": todo["title"],
            "completed": todo["completed"]
        }

        if user_id_str not in all_tasks:
            all_tasks[user_id_str] = []

        all_tasks[user_id_str].append(task_info)

    # Write to file
    with open("todo_all_employees.json", "w") as f:
        json.dump(all_tasks, f)

