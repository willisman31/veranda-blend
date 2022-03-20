import requests

games = []
site = 'https://www.espn.com/soccer/scoreboard'

response = requests.get(site)
body = str(response.content)
l = body.find(">Show All Leagues<")
r = body.rfind(',"zipcodes":{"')
print(body[l:r])


	
