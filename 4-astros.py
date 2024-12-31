from pip._vendor import requests

repsonse = requests.get("http://api.open-notify.org/astros.json")
json = repsonse.json()

print(repsonse)
print(json['people'])
print(json.get('people'))
