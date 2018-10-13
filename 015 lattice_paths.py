import itertools

#print list(itertools.product(['left','right'], ['left','right']))

a = [2,2]

def recPath(gridSize): #shamelessly stolen, solution was made beforehand, but this solution has an interesting algorithm
    """
    Recursive solution to grid problem. Input is a list of x,y moves remaining.
    """
    # base case, no moves left
    if gridSize == [0,0]: 
    	return 1
    # recursive calls
    paths = 0
    # move left when possible
    if gridSize[0] > 0:
        paths += recPath([gridSize[0]-1,gridSize[1]])
    # move down when possible
    if gridSize[1] > 0:
        paths += recPath([gridSize[0],gridSize[1]-1])
 
    return paths


import time
 
def route_num(cube_size):
    L = [1] * cube_size
    for i in range(cube_size):
        for j in range(i):
            L[j] = L[j]+L[j-1]
        L[i] = 2 * L[i - 1]
    return L[cube_size - 1]
 
start = time.time()
n = route_num(20)
elapsed = (time.time() - start)
print "%s found in %s seconds" % (n,elapsed)

