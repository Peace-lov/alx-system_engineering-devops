#!/usr/bin/python3
""" This is the python that gets an API and convert to JSON """

import csv
import json
import requests
import sys

if __name__ == '__main__':
    USER_ID = sys.argv[1]
    url_to_user = 'https://jsonplaceholder.typicode.com/users/' + USER_ID
    rs = requests.get(url_to_user)
    """documentation"""
    USERNAME = rs.json().get('username')
    """documentation"""
    url_to_tsk = url_to_user + '/todos'
    rs = requests.get(url_to_tsk)
    tsks = rs.json()

    dic_data = {USER_ID: []}
    for tsk in tsks:
        TASK_COMPLETED_STATUS = tsk.get('completed')
        TASK_TITLE = tsk.get('title')
        dic_data[USER_ID].append({
                                "task": TASK_TITLE,
                                "completed": TASK_COMPLETED_STATUS,
                                "username": USERNAME})
    """print(dic_data)"""
    with open('{}.json' .format(USER_ID), 'w') as f:
        json.dump(dic_data, f)
