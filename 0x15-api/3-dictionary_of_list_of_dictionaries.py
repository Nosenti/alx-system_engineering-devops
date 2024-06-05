#!/usr/bin/python3
"""A script to fetch TODO lists of all employees from JSONPlaceholder API
and export them to a JSON file."""
import requests
import json


def export_all_tasks_to_json():
    """Fetch tasks of all employees and export them to a JSON file."""
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        return "Failed to retrieve data"

    users = users_response.json()
    todos = todos_response.json()

    user_dict = {str(user['id']): [] for user in users}
    for todo in todos:
        user_dict[str(todo['userId'])].append({
            "username": next(user['username'] for user in users if
                             user['id'] == todo['userId']),
            "task": todo['title'],
            "completed": todo['completed']
        })

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile, indent=4)


if __name__ == "__main__":
    export_all_tasks_to_json()
