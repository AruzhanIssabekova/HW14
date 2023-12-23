import json
import requests

url = "https://jsonplaceholder.typicode.com/todos/"
response = requests.get(url)
inf = response.json()

with open('HW14.json', 'w') as file:
    json.dump(inf, file, indent=2)

with open('HW14.json', 'r') as file:
    loaded_data = json.load(file)

for i, item in enumerate(loaded_data, 1):
    filename = f'{i}.json'
    with open(filename, 'w') as todo_file:
        json.dump(item, todo_file, indent=2)