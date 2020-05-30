def solution(mapp):
	h = len(mapp)
	w = len(mapp[0])

	start_dist = djikstra(mapp, (0,0))
	finish_dist = djikstra(mapp, (h-1, w-1))

	min_dist = start_dist[h-1][w-1]

	for i in range(h):
		for j in range(w):
			if mapp[i][j] == 1:
				nbrs = [(i+k, j+l) for (k,l) in [(1,0), (-1,0), (0,1), (0,-1)]]

				nbrs = filter(lambda (i,j): (0<=i) and (i<h) and (0<=j) and (j<w) and (mapp[i][j] == 0), nbrs)

				if (i-1,j) in nbrs and (i+1,j) in nbrs:
					min_dist = min(min_dist, start_dist[i-1][j]+finish_dist[i+1][j]+2, start_dist[i+1][j]+finish_dist[i-1][j]+2)

				if (i,j-1) in nbrs and (i,j+1) in nbrs:
					min_dist = min(min_dist, start_dist[i][j-1]+finish_dist[i][j+1]+2, start_dist[i][j+1]+finish_dist[i][j-1]+2)

	return min_dist+1
    
def djikstra(mapp, startnode):
	map1 = [[mapp[x][y] for y in range(len(mapp[x]))] for x in range(len(mapp))]
	
	unvisited = []
	for i in range(len(map1)):
		for j in range(len(map1[i])):
			if map1[i][j] == 1:
				map1[i][j] = -1

			else:
				map1[i][j] = 500 # soft infinity. Works because biggest grid is 20 * 20
				unvisited.append((i,j))

	map1[startnode[0]][startnode[1]] = 0

	while len(unvisited) > 0:
		unvisited.sort(key=lambda x: map1[x[0]][x[1]], reverse=True)
		current = unvisited.pop()

		for (i,j) in neighbors(map1, current):
			map1[i][j] = min(map1[i][j], map1[current[0]][current[1]]+1)

	return map1

def neighbors(mapp, node):
	map1 = mapp
	list1 = [(node[0]+i, node[1]+j) for (i,j) in [(1,0), (-1,0), (0,1), (0,-1)]]

	def myfilter((i,j)):
		return (0<=i) and (i<len(map1)) and (0<=j) and (j<len(map1[0])) and (map1[i][j] != -1)

	list1 = filter(myfilter, list1)

	return list1