import sys
sys.path.append('./problems/')
import problemSolve
import problemSet
import elo
import user

#Problems
ps = problemSet.ProblemSet()
ps.addProblem(problemSolve.AdditionProblem())
ps.addProblem(problemSolve.MultiplicationProblem())
temp = problemSolve.Problem()
temp.prob="sqrt(4)"
temp.answer='2'
ps.addProblem(temp)
ps.addProblem(problemSolve.AlgebraProblem())

#User
currUser = user.User(0)
rank=elo.UserElo(0)
while (True):
	temp = ps.getProblem(rank.getElo())
	print('Your Rank: ' + str(currUser.getElo()));
	print('Problem Rank: ' + str(temp.elo.getElo()));	
	print(temp.getProblem())
	user_input = raw_input('>')
	if(user_input=='exit'):
		break
	elif (user_input==temp.answer):
		print("correct")
		ps.updateProblem(rank.getElo(),True)
		currUser.elo.updateElo(temp.elo.getElo(), True)
	else:
		print("incorrect")
		ps.updateProblem(rank.getElo(),False)
		currUser.elo.updateElo(temp.elo.getElo(), False)

