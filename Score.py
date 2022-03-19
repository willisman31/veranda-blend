import requests

class Game:

	games = []
	site = 'https://www.espn.com/soccer/scoreboard'

	__init__(self, home, away, network):
		self.home = home
		self.away = away
		self.network = network

	def retrieve(site):
		r = requests.get(site)
		return str(r)

	def clean(response):
		pass

	__repr__(self):
		return f'{self.home} vs {self.away} on {self.network}'


run()
	
