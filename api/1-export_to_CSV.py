#!/usr/bin/python3
"""Export TODO list for a given employee ID to CSV format."""
import csv
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    user_id = sys.argv[1]

    base_url = "https://jsonplaceholder.typicode.com/"

    # Get user info
    user = requests.get(f"{base_url}users/{user_id}").json()
    username = user.get("username")

    # Get all tasks for this user
    todos = requests.get(f"{base_url}todos", params={"userId": user_id}).json()

    # Create CSV file named USER_ID.csv in current directory
    filename = f"{user_id}.csv"
    with open(filename, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title")
            ])

