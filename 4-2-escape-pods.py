def BFS(path, s, t, parent):
    visited =[False]*len(path[0])
    queue=[]

    queue.append(s) 
    visited[s] = True

    while queue:
        u = queue.pop(0)

        for nbrIndex in range(len(path[u])):
            if path[u][nbrIndex] > 0 and not visited[nbrIndex]:
                queue.append(nbrIndex) 
                visited[nbrIndex] = True
                parent[nbrIndex] = u 


    return visited[t]

# Classic implementation of Ford-Fulkerson algorithm
def solution(entrances, exits, path):
    max_flow = 0

    augmentPathExists=True

    while augmentPathExists:
        augmentPathExists=False

        for source in entrances:
            for sink in exits:
                parent = [-1]*(len(path[0]))
                if BFS(path, source, sink, parent):
                    augmentPathExists = True

                    path_flow = float("inf")
                    s = sink

                    while(s !=  source): 
                        path_flow = min(path_flow, path[parent[s]][s]) 
                        s = parent[s]

                    max_flow +=  path_flow 

                    # Update residual capacities of the edges and reverse edges along the path 
                    v = sink 
                    while(v !=  source): 
                        u = parent[v] 
                        path[u][v] -= path_flow 
                        path[v][u] += path_flow 
                        v = parent[v] 

    return max_flow 