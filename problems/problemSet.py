import random

#Object with all the problems
#carries the rank and choose the problem to return
class ProblemSet:
	def __init__(self):
		self.problems=[]
		self.currentProblem = -1
	def addProblem(self,prob):
		self.problems.append(prob)
		index1 = 0
		index2 = len(self.problems)-1
		tempIndex=0
		while(index2>index1):
			tempIndex = (index2+index1)//2
			if(prob.elo.getElo() > self.problems[tempIndex].elo.getElo()):
				index1 = tempIndex
			elif(prob.elo.getElo() < self.problems[tempIndex].elo.getElo()):
				index2 = tempIndex
			else:
				index2=index1	
		self.problems.insert(tempIndex,prob)
			
	#returns a problem suitable for the rank of the user in a certain range of rank
	def getProblem(self, rank):
		index = random.randint(0,len(self.problems)-1)
		self.currentProblem = index
		return self.problems[index]
	#updates the placement of a problem if the rank is updated
	def updateProblem(self, rank, correct):
		self.problems[self.currentProblem].updateRank(rank,correct)
		temp = self.problems.pop(self.currentProblem)
		self.addProblem(temp)
		
