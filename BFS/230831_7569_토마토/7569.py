# 08:15 ~ 08:55
# 
# 알고리즘 : 3차원 BFS 문제를 구현하자

import sys
from copy import deepcopy
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(starting_tomatos, graph, visited):
    q = deque()
    
    for tomato in starting_tomatos:
        q.append((tomato[0],tomato[1],tomato[2], 0))
        visited[tomato[0]][tomato[1]][tomato[2]] = True
    
    while q:
        i,j,k,steps = q.popleft()

        for g in range(4):
            nx = dx[g] + j
            ny = dy[g] + k
            
            if 0<=nx<len(graph[0]) and 0<=ny<len(graph[0][0]):
                if graph[i][nx][ny] == 0 and visited[i][nx][ny] != True:
                    graph[i][nx][ny] = 1
                    visited[i][nx][ny] = True
                    q.append((i,nx,ny,steps+1))
                    
        if i+1<len(graph):
            if graph[i+1][j][k] == 0 and visited[i+1][j][k] != True:
                graph[i+1][j][k] = 1
                visited[i+1][j][k] = True
                q.append((i+1,j,k,steps+1))
                
        if 0<= i-1:
            if graph[i-1][j][k] == 0 and visited[i-1][j][k] != True:
                graph[i-1][j][k] = 1
                visited[i-1][j][k] = True
                q.append((i-1,j,k,steps+1))
    return steps
                 

m,n,h = map(int, input().split())


graph = []
for _ in range(h):
    tmp = []
    for _ in range(n):
        tmp.append(list(map(int, input().split())))
    graph.append(tmp)
    
# 모두 익지 못하는 상황을 대비해좌 -> deepcopy
check = deepcopy(graph)
visited = [[[False]*m for _ in range(n)] for _ in range(h)]

starting_tomato = []
for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 1:
                starting_tomato.append([a,b,c])

if len(starting_tomato) == 0:
    print(-1)
    sys.exit()

answer = bfs(starting_tomato, graph, visited)

for a in range(h):
    for b in range(n):
        for c in range(m):
            if graph[a][b][c] == 0:
                print(-1)
                sys.exit()
                
print(answer)
