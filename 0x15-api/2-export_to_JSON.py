#!/usr/bin/python3
""" 2-export_to_JSON.py """
import json
import requests
import sys


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com'
    id = sys.argv[1]
    username = json.loads(requests.get(f'{url}/users/{id}')
                          .text).get('username')
    tasks = json.loads(requests.get(f'{url}/todos?userId={id}').text)
    ctasks = [{"task": task.get('title'), "completed": task.get('completed'),
               "username": username} for task in tasks]
    with open(f'{id}.json', 'w') as jsonf:
        json.dump({f"{id}": ctasks}, jsonf)
