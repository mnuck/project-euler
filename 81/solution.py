# Euler 81
#
# Find the lowest cost path through a matrix

def main():
    with open('matrix.txt', 'r') as f:
        raw = f.read()
    matrix = [[int(x) for x in row.split(',')]
              for row in raw.split('\r\n')[:-1]]
    for i in xrange(1,len(matrix)):
        matrix[0][i] += matrix[0][i-1] # top edge
        matrix[i][0] += matrix[i-1][0] # left edge

    for i in xrange(1, len(matrix)):
        for j in xrange(1, len(matrix)):
                matrix[i][j] += min([ matrix[i-1][j], matrix[i][j-1] ])
    print matrix[-1][-1]

if __name__ == '__main__':
    main()
    
