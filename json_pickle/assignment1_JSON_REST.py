import requests
import json

response = requests.get('http://jsonplaceholder.typicode.com/todos')

todos = json.loads(response.text)
#print(todos)

for task in todos:
    if task['completed'] == True:
        print(task)