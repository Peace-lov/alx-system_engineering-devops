#!/usr/bin/python3
""" This is to export api to CSV """
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """anything"""
    user_name = res.json().get('username')
    tsk = url_user + '/todos'
    res = requests.get(tsk)
    tsks = res.json()

    with open('{}.csv' .format(user), 'w') as csvfile:
        for tsk in tsks:
            completed = tsk.get('completed')
            """complete"""
            title_tsk = tsk.get('title')
            """Done"""
            csvfile.write('"{}","{}","{}","{}"\n' .format(
                user, user_name, completed, title_tsk))
