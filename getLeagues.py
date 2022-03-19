import requests, json

# sport = "Soccer"
site = "https://www.espn.com/soccer/scoreboard"

headers = {'Content-type': 'application/json'}
data = ''

response = requests.get(site, headers=headers, data=data)
print(str(response))

