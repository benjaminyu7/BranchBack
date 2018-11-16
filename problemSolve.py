import random

#Problem object
class Problem:
	def __init__(self):
		self.rank = 1
	#gets or generates a problem
	def getProblem (self):
		return self.prob
	def getSolution (self):
		return self.answer
	#updates the ranking of the problem based on the user rank and correct or not
	def updateRank (self, rank, correct):
		pass
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
		x = random.randint(1,9//a)
		b = random.randint(1,9-a*x)
		self.prob="f(x)="+str(a)+'x+'+str(b) + "\nf("+str(x)+")"
		self.answer=str(a*x+b)
		return self.prob
		
#Object with all the problems
class ProblemSet:
	def __init__(self):
		self.problems=[]
	def addProblem(self,prob):
		self.problems.append(prob)
	#returns a problem suitable for the rank of the user in a certain range of rank
	def getProblem(self, rank):
		return self.problems[random.randint(0,len(self.problems)-1)]
	
#elo object that handles how much we should change elo for a person or problem
class Elo:
	def __init__(self):
		self.elo=0
	#updates the elo ranking based on the rank and the rise
	def updateElo(self, rank, rise):
		pass

ps = ProblemSet()
ps.addProblem(AdditionProblem())
ps.addProblem(MultiplicationProblem())
temp = Problem()
temp.prob="sqrt(4)"
temp.answer='2'
ps.addProblem(temp)
ps.addProblem(AlgebraProblem())
#current ranking
rank=1
while (True):
	temp = ps.getProblem(rank)
	print(temp.getProblem())
	user_input = raw_input('>')
	if (user_input==temp.answer):
		print("correct")
		temp.updateRank(rank, True)
	else:
		print("incorrect")
		temp.updateRank(rank, False)
		
