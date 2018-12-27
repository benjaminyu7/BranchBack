import elo

class User:
	def __init__(self, newElo):
		self.elo = elo.UserElo(newElo)
	def getElo(self):
		return self.elo.getElo()
