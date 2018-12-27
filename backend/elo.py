#elo object that handles how much we should change elo for a person or problem
class Elo:
	def __init__(self, elo):
		self.elo=elo
	#updates the elo ranking based on the rank and the rise
	def updateElo(self, rank, rise):
		pass
	def getElo(self):
		return self.elo

class ProblemElo(Elo):
	def updateElo(self, rank, rise):
		if (rise):
			if (rank >= self.elo):
				self.elo=self.elo+5
			else:
				self.elo=self.elo+1
		else:
			if (rank >= self.elo):
				self.elo=self.elo-1
			else:
				self.elo=self.elo-5

class UserElo(Elo):
	def __init__(self, elo):
		self.elo=elo
	def updateElo(self, rank, rise):
		if (rise):
			if (rank >= self.elo):
				self.elo=self.elo+5
			else:
				self.elo=self.elo+1
		else:
			if (rank >= self.elo):
				self.elo=self.elo-1
			else:
				self.elo=self.elo-5
