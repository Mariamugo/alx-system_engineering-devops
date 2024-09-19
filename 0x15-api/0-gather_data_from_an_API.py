#!/usr/bin/python3
"""
This script retrives employee data and todo tasks from an external API
endpoint and displays the employee name, the number of tasks completed
out the total tasks to be completed
"""

import sys
import requests


def employee_data(employee_id):
    url = "https://jsonplaceholder.typicode.com/"
    user_info = requests.get(url + "users/{}".format(employee_id)).json()
    todo = requests.get(url + "todos", params = {"userId": employee_id}).json()

    """variables to lists completed and total tasks"""
    completed = [t.get("title") for t in todo if t.get("completed") is True]
    total_todo = len(todo)
    comp_count = len(completed)

    return user_info.get("name"), comp_count, total_todo, completed


"""check whether script is imported or run directly"""
"""if script is run directly, execute code"""
"""if imported, don't execute code"""
if __name__ == "__main__":
    if len(sys.argv) != 2:
        """first command line arg passed to script"""
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    """script to accept integer param"""
    employee_id = int(sys.argv[1])
    employee_name, comp_count, total_todo, completed = employee_data(employee_id)

    print("Employee {} is done with tasks {}/{}:".format
        (employee_name, comp_count, total_todo))
    for task in completed:
        print("\t{}".format(task))

