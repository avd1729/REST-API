import requests

BASE = "http://127.0.0.1:5000/"

# response = requests.get(BASE + "greet")
# print(response.json())

response = requests.post(BASE + "greet")
print(response.json())
