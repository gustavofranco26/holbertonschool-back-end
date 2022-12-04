#!/usr/bin/python3
"""Return the information about an employee from an API
whose ID is passed into the script"""

from requests import get
from sys import argv


def get_api():
    """Data struct to api """
    employee_id = int(argv[1])
    employee_name = ""
    number_of_done_tasks = 0
    number_of_tasks = 0
    titles_of_tasks = []

    users_res = get("https://jsonplaceholder.typicode.com/users").json()

    for user in users_res:
        if (user['id']) == employee_id:
            employee_name = user['name']
            break

    tasks_res = get("https://jsonplaceholder.typicode.com/todos").json()

    for task in tasks_res:
        if (task['userId'] == employee_id):
            if task['completed']:
                titles_of_tasks.append(task['title'])
                number_of_done_tasks += 1
            number_of_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          number_of_done_tasks,
                                                          number_of_tasks))
    for title in titles_of_tasks:
        print("\t {}".format(title))


if __name__ == '__main__':
    get_api()
