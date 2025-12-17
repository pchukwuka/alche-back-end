#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Get user info
    user_url = f"{base_url}/users/{employee_id}"
    user_res = requests.get(user_url)
    user = user_res.json()
    employee_name = user.get("name")

    # Get todos for this user
    todos_url = f"{base_url}/todos"
    params = {"userId": employee_id}
    todos_res = requests.get(todos_url, params=params)
    todos = todos_res.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

