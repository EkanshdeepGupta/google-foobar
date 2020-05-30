dict_soln = {}

def solution(n):
    solution = 0
    for stair in range(2, n):
    	temp = dyn_soln(n, stair)
    	solution += temp
    return solution

def dyn_soln(bricks, stairs):
	if (bricks, stairs) in dict_soln.keys():
		return dict_soln[(bricks, stairs)]

	else:
		if bricks < ((stairs * (stairs+1)) / 2):
			dict_soln[(bricks, stairs)] = 0
			return 0
		if stairs==1:
			dict_soln[(bricks, stairs)] = 1
			return 1

		else:
			count = 0
			for i in range(1, bricks/stairs+1):
				count += dyn_soln((bricks - i*stairs), (stairs-1))

			dict_soln[(bricks, stairs)] = count
			return count