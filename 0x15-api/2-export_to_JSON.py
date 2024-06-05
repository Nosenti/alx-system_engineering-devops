#!/usr/bin/python3
"""A script to fetch TODO list of an employee from JSONPlaceholder
API and export it to a JSON file."""
import json
import requests
import sys


def export_tasks_to_json(employee_id):
    """Fetch tasks of an employee and export them to a JSON file."""
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"
    todos_url = f"{base_url}/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return "Failed to retrieve data"

    user = user_response.json()
    todos = todos_response.json()

    with open(f"{employee_id}.json", 'w') as jsonfile:
        tasks = []
        for task in todos:
            task_dict = {
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user.get('username')
            }
            tasks.append(task_dict)
        json.dump({str(employee_id): tasks}, jsonfile)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./2-export_to_JSON.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_tasks_to_json(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID")
