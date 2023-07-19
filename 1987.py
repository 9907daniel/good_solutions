# 09:27  ~ 10:09
#
# R,C 의 길이 -> 20
# 20! -> DFS 완탐이 가능할듯하다
#
# 풀이 1) DFS 아슬아슬한 TLE인듯 -> 65% 
#
#
#
#########################

# from collections import deque
# r,c = map(int, input().split())
# graph = []
# for _ in range(r):
#     graph.append(list(input()))
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
# visited = [[False]*c for _ in range(r)]
# stack = []

# stack.append(graph[0][0])
# current_max = 0

# def bfs(x,y, count):
#     q = deque()
#     q.append((x,y,count))
    
#     while q:
#         x,y, steps = q.pop()
#         print(steps)
        
#         for a in range(4):
#             nx = dx[a]+x
#             ny = dy[a]+y
            
#             if 0<=nx<r and 0<=ny<c:
#                 if visited[nx][ny] != True and graph[nx][ny] not in stack:
#                     visited[nx][ny] = True
#                     stack.append(graph[nx][ny])
#                     q.append((nx,ny,steps+1))
# bfs(0,0,1)
# print(current_max)





##########################

r,c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(input()))
    
dx = [-1,1,0,0]
dy = [0,0,-1,1]
stack = set(graph[0][0])
current_max = 0

def dfs(x,y, count):
    global current_max
    current_max = max(current_max, count)
    
    for a in range(4):
        nx = dx[a]+x
        ny = dy[a]+y
        
        if 0<=nx<r and 0<=ny<c:
            if graph[nx][ny] not in stack:
                stack.add(graph[nx][ny])
                dfs(nx,ny, count+1)
                stack.remove(graph[nx][ny])


dfs(0,0,1)
print(current_max)












