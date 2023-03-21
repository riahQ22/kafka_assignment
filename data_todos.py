import json

with open ('todos.json','r') as t:
    get_todos = json.load(t)

print(get_todos)