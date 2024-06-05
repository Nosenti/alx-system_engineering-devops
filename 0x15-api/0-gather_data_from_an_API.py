#!/usr/bin/python3
"""A script to fetch TODO list progress of en employee"""
import requests
import sys


def fetch_todo_list_progress(employee_id):
    """fetch and display TODO list progress of an employee given their ID"""
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"
    todos_url = f"{base_url}/{employee_id}/todos"
    user_res = requests.get(user_url)
    todos_res = requests.get(todos_url)
    if user_res.status_code != 200 or todos_res.status_code != 200:
        return "Failed to retrieve data"
    user = user_res.json()
    todos = todos_res.json()
    completed_tasks = [todo for todo in todos if todo.get("completed") is True]
    total_tasks = len(todos)
    print(
        f"Employee {user.get('name')} is done with tasks("
        f"{len(completed_tasks)}/{total_tasks}):"
    )
    for task in completed_tasks:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            fetch_todo_list_progress(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID")
