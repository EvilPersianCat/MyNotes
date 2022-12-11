from collections import deque

n,m  = map(int, input().split())
matrix = []
d = [ [-1] * m for _ in range(n) ]
for i in range(n):
    matrix.append( list( map(int, input().split() ) ) )

def bfs():
    dir = [ [-1,0], [0,1], [1,0], [0,-1] ]
    queue = deque()
    queue.append( (0,0) )
    d[0][0] = 0
    while queue:
        t = queue.popleft()
        for i in range(4):
            x, y = t[0] + dir[i][0], t[1] + dir[i][1]
            if x < n and y < m and x >=0 and y >= 0 and d[x][y] == -1 and matrix[x][y] == 0:
                queue.append( (x, y) )
                d[x][y] = d[ t[0] ][  t[1] ] + 1
    
    # return d[-1][-1]
    return d[-1][-1]



if __name__ == '__main__':
    print( bfs() )