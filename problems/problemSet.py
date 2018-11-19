import random

#Object with all the problems
class ProblemSet:
	def __init__(self):
		self.problems=[]
	def addProblem(self,prob):
		self.problems.append(prob)
	#returns a problem suitable for the rank of the user in a certain range of rank
	def getProblem(self, rank):
		return self.problems[random.randint(0,len(self.problems)-1)]
