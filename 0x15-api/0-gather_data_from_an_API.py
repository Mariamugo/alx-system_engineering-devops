#!/usr/bin/python3
"""using the requests module"""
import requests
"""access command line arguments"""
import sys
"""API endpoint resource -- access employee data & todo list"""
url = https://jsonplaceholder.typicode.com/


"""introducing function with employee ID & todo variables"""
def employee_data(employee_id):
    user_info = requests.get(url + "users/{}".format(employee_id)).json()
    todo_list = requests.get(url + "todos", params={"user_id": employee_id}).json()

    """variables to lists completed and total tasks"""
    completed = [task.get("title") for task in todo_list if task.get("completed")]
    total_todos = len(todo_list)
    completed_todo_number = len(completed)

    return user_info.get("name"), completed_todo_number, total_todos, completed


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
    employee_name, completed_todo_number, total_todos, completed = employee_data(employee_id)


    print("Employee {} is done with tasks {}/{}:".format(employee_name, completed_todo_number, total_todos))
    for task in  completed:
        print("\t", task)
