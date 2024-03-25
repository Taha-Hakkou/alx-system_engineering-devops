#!/usr/bin/python3
""" 3-dictionary_of_list_of_dictionaries.py """
import json
import requests


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    uids = [usr.get('id') for usr
            in json.loads(requests.get(f'{url}/users').text)]
    tasks = {}
    for id in uids:
        username = json.loads(requests.get(f'{url}/users/{id}')
                              .text).get('username')
        ptasks = json.loads(requests.get(f'{url}/todos?userId={id}').text)
        ctasks = [{"username": username, "task": task.get('title'),
                   "completed": task.get('completed')} for task in ptasks]
        tasks[f"{id}"] = ctasks
    with open('todo_all_employees.json', 'w') as jsonf:
        json.dump(tasks, jsonf)
