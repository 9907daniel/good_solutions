# 01:20 ~ 01:33
#
# 최단거리 : BFS가 더 적합할듯 하다
#

from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

results = []

def bfs(n,m,maps, visited):
    visited[0][0] = False
    q = deque()
    q.append((0,0,1))
    
    while q:
        x,y,count = q.popleft()
        maps[x][y] = count
        for a in range(4):
            nx = dx[a]+x
            ny = dy[a]+y
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] != True and maps[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx,ny, count+1))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    bfs(n,m,maps, visited)
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    
    
    
    