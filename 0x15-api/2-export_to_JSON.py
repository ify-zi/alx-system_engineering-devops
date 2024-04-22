#!/usr/bin/python3
"""
    API request modules
"""

import json
import requests
import sys


if __name__ == '__main__':

    test_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_info = requests.get(test_url + "users/{}".format(user_id)).json()
    todos_info = requests.get(test_url + "todos",
                              params={'user_id': user_id}).json()
    dict_values = {user_id: [
                             {'title': todo.get('title'),
                              'completed': todo.get('completed'),
                              'username': user_info.get('username')
                             } for todo in todos_info[:20]]}
    with open("{}.json".format(user_id), "w", newline="") as j_file:
        json.dump(dict_values, j_file)
