import requests

BASE = "http://127.0.0.1:5000/"

# Put request to add a video
response = requests.put(
    BASE + "video/1", json={"name": "xyz", "views": 990, "likes": 99})
print(response.json())

# Get request to retrieve the video data
response = requests.get(BASE + "video/1")
print(response.json())
