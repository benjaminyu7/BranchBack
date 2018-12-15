import sys
sys.path.append('../problems/')
sys.path.append('..')
import problemSet
import problemSolve
import unittest
import elo

class TestProblemSet(unittest.TestCase):
	def testGetProblem(self):
		ps = problemSet.ProblemSet()
		#initialize problems
		prob1 = problemSolve.Problem()
		prob1.elo = elo.ProblemElo(1)
		prob2 = problemSolve.Problem()
		prob2.elo = elo.ProblemElo(2)
		prob3 = problemSolve.Problem()
		prob3.elo = elo.ProblemElo(3)
		prob4 = problemSolve.Problem()
		prob4.elo = elo.ProblemElo(4)
		
		#add problems to set
		ps.addProblem(prob4)
		ps.addProblem(prob3)
		ps.addProblem(prob1)
		ps.addProblem(prob2)

		self.assertEqual(ps.getProblem(2).elo.getElo(), 2)
		self.assertEqual(ps.getProblem(4).elo.getElo(), 4)
		self.assertEqual(ps.getProblem(1).elo.getElo(), 1)
	def testAddProblem(self):
		ps = problemSet.ProblemSet()
		prob1 = problemSolve.Problem()
		prob1.elo = elo.ProblemElo(1)
		prob2 = problemSolve.Problem()
		prob2.elo = elo.ProblemElo(2)
		prob3 = problemSolve.Problem()
		prob3.elo = elo.ProblemElo(3)
		prob4 = problemSolve.Problem()
		prob4.elo = elo.ProblemElo(4)
		ps.addProblem(prob4)
		ps.addProblem(prob3)
		ps.addProblem(prob1)
		ps.addProblem(prob2)
		ps.addProblem(prob2)
		ps.addProblem(prob1)
		ps.addProblem(prob4)
		self.assertEqual(ps.getElo(), [1,1,2,2,3,4,4])




if __name__=='__main__':
	unittest.main()
