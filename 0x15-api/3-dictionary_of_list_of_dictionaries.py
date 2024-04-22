#!/usr/bin/python3
"""Python cript that fetch Rest API fo todo lists of employees"""

import json
import requests
import sys

if __name__ == '__main__':
    url = "https://jsonplaceholder.typicode.com/users"

    rsp = requests.get(url)
    Users = rsp.json()

    users_dic = {}
    for user in Users:
        USER_ID = user.get('id')
        USERNAME = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}' .format(USER_ID)
        url = url + '/todos/'
        rsp = requests.get(url)

        tsks = rsp.json()
        users_dic[USER_ID] = []
        for tsk in tsks:
            TASK_COMPLETED_STATUS = tsk.get('completed')
            TASK_TITLE = tsk.get('title')
            users_dic[USER_ID].append({
                "task": TASK_TITLE,
                "completed": TASK_COMPLETED_STATUS,
                "username": USERNAME
            })
            """SOMETHING LITTLE"""
    with open('todo_all_employees.json', 'w') as f:
        json.dump(users_dic, f)
