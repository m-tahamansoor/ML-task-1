import requests
import json

url = "https://reqres.in/"

response = requests.get(url + "/api/users?page=2").json()

data = response["data"]

ids = []
emails = []

for required_data in data:
    ids.append(required_data['id'])
    emails.append(required_data['email'])

for email,id in zip(emails,ids):
    print(f"ID: {id}, Email: {email}")