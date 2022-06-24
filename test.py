# %%

import requests

api_url = "http://localhost:9002/api/mail2rajja@gmail.com/tasks"
todo = {"title": "Buy milk", "completed": False}
response = requests.post(api_url, json=todo)
response.json()

# {'userId': 1, 'title': 'Buy milk', 'completed': False, 'id': 201}

# >>> response.status_code
