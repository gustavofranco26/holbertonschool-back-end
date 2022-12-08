#!/usr/bin/python3
"""
Using a REST API, for a given employee ID,
returns information about his/her DOTO .
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    b_url = 'https://jsonplaceholder.typicode.com/users/'
    u_id = argv[1]
    f_msg = 'Employee {} is done with tasks({}/{}):'

    u_url = '{}{}'.format(b_url, u_id)
    todo_url = '{}{}/todos'.format(b_url, u_id)
    completed_tasks_url = '{}?completed=true'.format(todo_url)

    user = get(u_url).json()
    all_tasks = get(todo_url).json()
    completed_tasks = get(completed_tasks_url).json()

    name = user.get('name')
    total_tasks = len(all_tasks)
    done_tasks = len(completed_tasks)

    print(final_msg.format(name, done_tasks, total_tasks))

    for task in completed_tasks:
        print('\t {}'.format(task.get("title")))
