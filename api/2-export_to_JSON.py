#!/usr/bin/python3
import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
    )

    user_data = requests.get(user_url).json()
    employee_username = user_data.get("username")

    todos = requests.get(todos_url).json()

    task_list = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_username
        }
        for task in todos
    ]

    output = {user_id: task_list}

    with open(f"{user_id}.json", "w") as json_file:
        json.dump(output, json_file)
