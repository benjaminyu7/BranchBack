import sys
sys.path.append('..')
import elo
import unittest

class TestElo(unittest.TestCase):
	def testProblemElo(self):
		problem = elo.ProblemElo(0)
		problem.updateElo(1, True)
		self.assertEqual(problem.getElo(), 5)
		problem.updateElo(1, True)
		self.assertEqual(problem.getElo(), 6)

		problem.updateElo(1, False)
		self.assertEqual(problem.getElo(), 1)
		problem.updateElo(2, False)
		self.assertEqual(problem.getElo(), 0)

	def testUserElo(self):
		user = elo.ProblemElo(0)
		user.updateElo(1, True)
		self.assertEqual(user.getElo(), 5)
		user.updateElo(1, True)
		self.assertEqual(user.getElo(), 6)

		user.updateElo(1, False)
		self.assertEqual(user.getElo(), 1)
		user.updateElo(2, False)
		self.assertEqual(user.getElo(), 0)


if __name__=='__main__':
	unittest.main()
