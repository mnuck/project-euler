# Euler 83
#
# Find the cost of the lowest cost path from upper left to lower right

from heapq import heappush as push
from heapq import heappop as pop

def main():
    with open('matrix.txt', 'r') as f:
        raw = f.read()
    matrix = [[int(x) for x in row.split(',')]
              for row in raw.split('\r\n')[:-1]]
    length = len(matrix)
    weights = dict()
    for i in xrange(length):
        for j in xrange(length):
            weights[(i,j)] = -1

    weights[(0,0)] = matrix[0][0]
    frontier = list()
    push(frontier, (weights[(0,0)], (0,0)))
         
    while len(frontier) > 0:
        _, (x,y) = pop(frontier)
        if (x,y) == (length-1, length-1):
            break
        for (i,j) in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
            if (i,j) in weights and weights[(i,j)] == -1:
                weights[(i,j)] = weights[(x,y)] + matrix[i][j]
                push(frontier, (weights[(i,j)], (i,j)))
    
    print weights[(length-1, length-1)]
    
if __name__ == '__main__':
    main()
