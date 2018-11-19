import sys
sys.path.append('./problems/')
import problemSolve
import problemSet

ps = problemSet.ProblemSet()
ps.addProblem(problemSolve.AdditionProblem())
ps.addProblem(problemSolve.MultiplicationProblem())
temp = problemSolve.Problem()
temp.prob="sqrt(4)"
temp.answer='2'
ps.addProblem(temp)
ps.addProblem(problemSolve.AlgebraProblem())
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
		
