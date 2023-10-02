# 09:25 ~ 
# 
# 입출력)
# 5x5 이기 때문에 백트래킹, 완탐, DFS/BFS 등 전부 가능할듯 하다
# 
# 1) 모든 경우를 iterate하고 조합을 구한다, 여기서 x,y기준으로 정렬을 하고 만약 이미 존재한다면 countX
# 
#

from itertools import combinations
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for _ in range(5):
    graph.append(list(input()))
    
already_counted = []
count = 0
    
def check(graph, visited,l,x,y):
    global count
    
    tried =[[False]*5 for _ in range(5)]
    
    q = deque()
    q.append((x,y))
    steps = 0   
    tried[x][y] = True
   
    team_member = 0 
    
    while q:
        i,j = q.popleft()
        tried[i][j] = True
        steps += 1

        if graph[i][j] == 'S':
            team_member += 1
    
        if steps == 7:
            if team_member >= 4:
                count += 1
            return
        
        for a in range(4):    
            nx = dx[a] + i
            ny = dy[a] + j
            
            if 0<=nx<5 and 0<=ny<5:
                if tried[nx][ny] != True and visited[nx][ny] == True:
                    tried[nx][ny] = True
                    q.append((nx,ny))
    return
                    
                    

all = []
for a in range(5):
    for b in range(5):
        all.append([a,b])

for a in combinations(all, 7):
    visited = [[False]*5 for _ in range(5)]
    for b in range(len(a)):
        visited[a[b][0]][a[b][1]] = True

    check(graph, visited, a, a[b][0],a[b][1])

print(count)

 

# from copy import deepcopy

# dx = [-1,1,0,0]
# dy = [0,0,-1,1]

# already_counted = []
# count = 0

# def combinations(graph, visited,x,y, tmp):
#     global count
#     # visited[x][y] = True
    
#     if len(tmp) >= 7:
#         compare = deepcopy(tmp)
#         compare.sort(key=lambda x: (x[0],x[1]))
#         if compare not in already_counted:
#             already_counted.append(compare[:])
#             tmp_count = 0
#             for j in range(len(compare)):
#                 if graph[compare[j][0]][compare[j][1]] == 'S':
#                     tmp_count += 1
#             if tmp_count >= 4:
#                 count += 1
#         return
    
#     for a in range(4):    
#         nx = dx[a] + x
#         ny = dy[a] + y
        
#         if 0<=nx<5 and 0<=ny<5:
#             if [nx,ny] not in tmp:
#                 tmp.append([nx,ny])
#                 combinations(graph, visited, nx,ny, tmp)
#                 tmp.pop()
#     return

# graph = []
# for _ in range(5):
#     graph.append(list(input()))

# for a in range(5):
#     for b in range(5):
#         visited = [[False]*5 for _ in range(5)]
#         tmp = []
#         combinations(graph, visited, a,b, tmp)
        
# print(count)

# YYYYY FFFTF
# SYSYS TFTTT
# YYYYY FFFTF
# YSYYS FFFTF
# YYYYY FFFFF

