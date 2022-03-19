import requests

r = requests.get('https://www.espn.com/soccer/scoreboard')
print(str(r.content))
