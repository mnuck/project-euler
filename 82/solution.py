# Euler 82
#
# Find the cost of the lowest cost horizontal seam through a matrix

from sys import maxint

def main():
    with open('matrix.txt', 'r') as f:
        raw = f.read()
    matrix = [[int(x) for x in row.split(',')]
              for row in raw.split('\r\n')[:-1]]
    length = len(matrix)
    path = list()
    for i in xrange(length):
        path.append( list() )
        for j in xrange(length):
            path[-1].append({})
            
    for i in xrange(length):
        path[i][0]['min'] = matrix[i][0] # left edge

    for j in xrange(1, length):
        # might have come from the left
        for i in xrange(length):
            path[i][j]['left'] = path[i][j-1]['min'] + matrix[i][j]
            
        # might have come from above
        path[0][j]['up'] = maxint
        for i in xrange(1,length):
            up = path[i-1][j]
            path[i][j]['up'] = min([up['left'], 
                                    up['up']]) + matrix[i][j]
            
        # might have come from below
        path[-1][j]['down'] = maxint
        for i in xrange(length-2,-1,-1):
            down = path[i+1][j]
            path[i][j]['down'] = min([down['left'], 
                                      down['down']]) + matrix[i][j]
            
        # so which one was it?
        for i in xrange(length):
            cell = path[i][j]
            cell['min'] = min([cell['left'], cell['up'], cell['down']])
    
    right_edge = [row[-1]['min'] for row in path]
    solution = min( right_edge )
    print solution

if __name__ == '__main__':
    main()
    
