# 10:09 ~ 10:23
# 그냥 BFS
#
#

from collections import deque



m,n = map(int, input().split())

graph = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(n):
    graph.append(list(input()))

visited = [[False]*m for _ in range(n)]

def bfs(x,y):
    q = deque()
    q.append((x,y,1))
    visited[x][y] = True

    c = 0

    while q:
        i,j, steps = q.popleft()
        c += 1
        for a in range(4):
            nx = dx[a]+i
            ny = dy[a]+j
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] != True and graph[nx][ny] == graph[i][j]:
                    visited[nx][ny] = True
                    q.append((nx,ny,steps+1))
    return c

black = 0
white = 0

for a in range(n):
    for b in range(m):
        if visited[a][b] != True:
            power = bfs(a,b)
            if graph[a][b] == 'B':
                black += power*power
            else:
                white += power*power
                
print(white, black)