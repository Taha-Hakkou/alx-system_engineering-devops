#!/usr/bin/python3
""" 0-gather_data_from_an_API.py """
import json
import requests
import sys


url = 'https://jsonplaceholder.typicode.com'
id = sys.argv[1]
name = json.loads(requests.get(f'{url}/users/{id}').text).get('name')
tasks = json.loads(requests.get(f'{url}/todos?userId={id}').text)
done = list(filter(lambda x: x.get('completed'), tasks))
print(f'Employee {name} is done with tasks({len(done)}/{len(tasks)}):')
for task in done:
    print(f"\t {task.get('title')}")
