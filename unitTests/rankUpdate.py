import sys
sys.path.append('../problems/')
sys.path.append('..')
import problemSet
import problemSolve
import unittest
import elo

class TestProblemSet(unittest.TestCase):
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
		ps.addProblem(prob3)
		ps.addProblem(prob1)
		ps.addProblem(prob2)
		ps.addProblem(prob2)
		ps.addProblem(prob1)
		ps.addProblem(prob4)
		self.assertEqual(ps.getElo(), [1,1,2,2,3,4])

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

		self.assertEqual(ps.getProblem(4).elo.getElo(), 4)
		self.assertEqual(ps.getProblem(1).elo.getElo(), 1)
		self.assertEqual(ps.getProblem(2).elo.getElo(), 2)

	def testUpdate(self):
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
		
		#testProblems
		ps.currentProblem = 0
		ps.updateProblem(4, True)
		self.assertEqual(ps.getElo(), [0,2,3,4])
		ps.updateProblem(4, False)
		self.assertEqual(ps.getElo(), [2,3,4,5])
		ps.currentProblem = 1
		ps.updateProblem(4, False)
		self.assertEqual(ps.getElo(), [2,4,5,8])
		ps.updateProblem(3, True)
		self.assertEqual(ps.getElo(), [-1,2,5,8])

if __name__=='__main__':
	unittest.main()
