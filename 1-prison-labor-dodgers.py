def solution(x, y):
    x.sort()
    y.sort()
   
    xExtra = len(x) > len(y)
    minSize = min(len(x), len(y))
   
    for a in range(minSize):
        if x[a] != y[a]:
            if xExtra:
                return x[a]

            else:
                return y[a]
    
    if xExtra:
        return x[-1]
    else:
        return y[-1]