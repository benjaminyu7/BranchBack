import random
import elo

#Problem object
class Problem:
	def __init__(self):
		self.elo = elo.ProblemElo(0)
	#gets or generates a problem
	def getProblem (self):
		return self.prob
	def getSolution (self):
		return self.answer
	#updates the ranking of the problem based on the user rank and correct or not
	def updateRank (self, userRank, correct):
		self.elo.updateElo(userRank, not correct)
	def saveProblem (self):
		return self

#generates a addition problem that uses one digit
class AdditionProblem(Problem):
	def getProblem(self):
		int1=random.randint(1,5)
		int2=random.randint(1,9-int1)
		self.prob=str(int1)+'+'+str(int2)
		self.answer=str(int1+int2)
		return self.prob

class SubtractionProblem(Problem):
	def getProblem(self):
		pass

#generates a single digit multiplication problem
class MultiplicationProblem(Problem):
	def getProblem(self):
		int1=random.randint(1,3)
		int2=random.randint(1,9//int1)
		self.prob=str(int1)+'*'+str(int2)
		self.answer=str(int1*int2)
		return self.prob

class DivisionProblem(Problem):
	def getProblem(self):
		pass

#f(x) = ax + b
class AlgebraProblem(Problem):
	def getProblem(self):
		a = random.randint(1,3)
		x = random.randint(1,8//a)
		b = random.randint(1,9-a*x)
		self.prob="f(x)="+str(a)+'x+'+str(b) + "\nf("+str(x)+")"
		self.answer=str(a*x+b)
		return self.prob
