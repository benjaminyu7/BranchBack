import random
import elo

#Problem object
class Problem(object):
	def __init__(self):
		self.elo = elo.ProblemElo(0)
		self.description = ""
	def __str__(self):
		converted= self.description + "\n" + str(self.elo.getElo())
		return converted
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
	def __init__(self):
		Problem.__init__(self)
		self.description = "Single digit addition"
	def getProblem(self):
		int1=random.randint(1,5)
		int2=random.randint(1,9-int1)
		self.prob=str(int1)+'+'+str(int2)
		self.answer=str(int1+int2)
		return self.prob

class SubtractionProblem(Problem):
	def __init__(self):
		Problem.__init__(self)
		self.description = "Single digit subtraction"
	def getProblem(self):
		pass

#generates a single digit multiplication problem
class MultiplicationProblem(Problem):
	def __init__(self):
		Problem.__init__(self)
		self.description = "Single digit multiplication"
	def getProblem(self):
		int1=random.randint(1,3)
		int2=random.randint(1,9//int1)
		self.prob=str(int1)+'*'+str(int2)
		self.answer=str(int1*int2)
		return self.prob

class DivisionProblem(Problem):
	def __init__(self):
		Problem.__init__(self)
		self.description = "Single digit division"
	def getProblem(self):
		pass

#f(x) = ax + b
class AlgebraProblem(Problem):
	def __init__(self):
		Problem.__init__(self)
		self.description = "Single digit algebra"
	def getProblem(self):
		a = random.randint(1,3)
		x = random.randint(1,8//a)
		b = random.randint(1,9-a*x)
		self.prob="f(x)="+str(a)+'x+'+str(b) + "\nf("+str(x)+")"
		self.answer=str(a*x+b)
		return self.prob
