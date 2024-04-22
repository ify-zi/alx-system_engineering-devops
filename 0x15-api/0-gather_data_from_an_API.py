#!/usr/bin/python3
"""
    API request modules
"""

import requests
from sys import argv


if __name__ == '__main__':
    
    test_url = 'https://jsonplaceholder.typicode.com/'
    user_id = argv[1]
    user_info = requests.get(test_url + "users/{}".format(user_id)).json()
    todos_info = requests.get(test_url + "todos", params={'user_id': user_id}).json()

    tasks = [t.get('title') for t in todos_info if t.get('completed') is True]
    print("Employee {} is done with task ({}/{})".format(user_info.get('name'),
                                                        len(tasks),
                                                        len(todos_info)))
    [print("\t {}".format(i)) for i in tasks]
