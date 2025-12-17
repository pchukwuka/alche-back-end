.
rts TODO list data for a given employee to JSON.
"""

import json
#!/usr/bin/python3
"""
Exports TODO list data for a given employee to JSON.
""

import json
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]

    # Base URLs
    url_user = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    # Fetch user info
    user_res = requests.get(url_user)
    user = user_res.json()
    username = user.get("username")

    # Fetch todos
    todos_res = requests.get(url_todos)
    todos = todos_res.json()

    # Build the list of tasks
    tasks_list = []
    for task in todos:
        tasks_list.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        })

    # Final data structure
    data = {user_id: tasks_list}

    # Write to JSON file USER_ID.json
    filename = f"{user_id}.json"
    with open(filename, "w") as f:
        json.dump(data, f)
