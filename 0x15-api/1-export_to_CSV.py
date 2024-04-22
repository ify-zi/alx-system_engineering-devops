#!/usr/bin/python3
"""
    API request modules
"""

import csv
import requests
import sys


if __name__ == '__main__':

    test_url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_info = requests.get(test_url + "users/{}".format(user_id)).json()
    todos_info = requests.get(test_url + "todos",
                              params={'user_id': user_id}).json()

    tasks = [t.get('title') for t in todos_info if t.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(user_info.get("name"), len(tasks), len(todos_info)))
    [print("\t {}".format(i)) for i in tasks]

    with open("{}.csv".format(user_id), 'w', encoding='utf-8') as exp:
        writer = csv.writer(exp, quoting=csv.QUOTE_ALL)
        [writer.writerow(
                         [user_id,
                         user_info.get("username"),
                         t.get("completed"),
                         t.get("title")]
                         ) for t in todos_info]
