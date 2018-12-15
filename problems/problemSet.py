import random

#Object with all the problems
#carries the rank and choose the problem to return
class ProblemSet:
	def __init__(self):
		self.problems=[]
		self.currentProblem = -1
	def findIndex(self, rank):
		index1 = 0
		index2 = len(self.problems)-1
		tempIndex=0
		if(len(self.problems)==0):
			return 0
		elif(self.problems[0].elo.getElo() > rank):
			return 0
		elif(self.problems[len(self.problems)-1].elo.getElo() < rank):
			return len(self.problems)
		while(index2>index1):
			tempIndex = (index2+index1)//2
			if(rank > self.problems[tempIndex].elo.getElo()):
				index1 = tempIndex + 1
			elif(rank < self.problems[tempIndex].elo.getElo()):
				index2 = tempIndex - 1
			else:
				index2=index1	
		if(self.problems[tempIndex].elo.getElo() < rank):
			tempIndex += 1
		return tempIndex
	def addProblem(self,prob):
		tempIndex = self.findIndex(prob.elo.getElo())
		self.problems.insert(tempIndex,prob)
	#returns a problem suitable for the rank of the user in a certain range of rank
	def getProblem(self, rank):
		index = self.findIndex(rank)
		if(index>len(self.problems)-1):
			return None
		self.currentProblem = index
		return self.problems[index]
	#updates the placement of a problem if the rank is updated
	def updateProblem(self, rank, correct):
		self.problems[self.currentProblem].updateRank(rank,correct)
		temp = self.problems.pop(self.currentProblem)
		self.addProblem(temp)
	def getElo(self):
		elos = []
		for x in self.problems:
			elos.append(x.elo.getElo())
		return elos
