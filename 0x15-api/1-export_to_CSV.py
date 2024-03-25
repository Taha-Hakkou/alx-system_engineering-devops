#!/usr/bin/python3
""" 1-export_to_CSV.py """
import csv
import json
import requests
import sys


url = 'https://jsonplaceholder.typicode.com'
id = sys.argv[1]
username = json.loads(requests.get(f'{url}/users/{id}').text).get('username')
tasks = json.loads(requests.get(f'{url}/todos?userId={id}').text)
for task in tasks:
    task['username'] = username
fields = ['userId', 'username', 'completed', 'title']
with open(f'{id}.csv', 'w') as csvf:
    writer = csv.DictWriter(csvf, delimiter=',', fieldnames=fields,
                            extrasaction='ignore', quoting=csv.QUOTE_ALL)
    writer.writerows(tasks)
