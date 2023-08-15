#
# 09:36 ~ 10:05
#
# 치즈로 둘쌓인 곳  : 벽을 만질 수 있다면 녹이는 공기다
#

from collections import deque
from copy import deepcopy

n,m = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(x,y, graph, visited, remove):
    before_change = deepcopy(graph)
    
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    
    while q:
        i,j = q.popleft()
        
        for a in range(4):
            nx = dx[a]+i
            ny = dy[a]+j
            
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0 and visited[nx][ny] != True:
                q.append((nx,ny))
                visited[nx][ny] = True
            if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 1:
                remove[nx][ny] = True
    return graph, remove, before_change
        
count = 1
while True:

    visited = [[False]*m for _ in range(n)]
    remove = [[False]*m for _ in range(n)]

    graph, remove, before_change = bfs(0,0, graph, visited, remove)
    
    non_cheese_count = 0
    for a in range(n):
        for b in range(m):
            if remove[a][b] == True:
                graph[a][b] = 0
            
            if graph[a][b] == 0:
                non_cheese_count += 1

    if non_cheese_count == n*m:
        steps = 0
        island_visited = [[False]*m for _ in range(n)]
        for a in range(n):
            for b in range(m):
                if before_change[a][b] == 1:
                    steps += 1
        break
    count += 1
    
print(count)
print(steps)
