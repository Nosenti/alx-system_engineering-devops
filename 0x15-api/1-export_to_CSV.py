#!/usr/bin/python3
"""A script to fetch TODO list of an employee from JSONPlaceholder API
and export it to a CSV file."""
import csv
import requests
import sys


def export_tasks_to_csv(employee_id):
    """Fetch tasks of an employee and export them to a CSV file."""
    base_url = "https://jsonplaceholder.typicode.com/users"
    user_url = f"{base_url}/{employee_id}"
    todos_url = f"{base_url}/{employee_id}/todos"

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        return "Failed to retrieve data"

    user = user_response.json()
    todos = todos_response.json()

    with open(f"{employee_id}.csv", 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow([employee_id,
                                 user.get('username'), task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./1-export_to_CSV.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            export_tasks_to_csv(employee_id)
        except ValueError:
            print("Please provide a valid integer for the employee ID")
