#
# 09:24 ~ 10:01 + 10:51 ~
#
# 입출력 : n = 200, M, 1000
#
#
# BFS를 사용한 이유 : 입출력값이 생각보다 높다, 찾으면 즉시 Return 하고 싶다
# 1) 24% 에서 메모리 초과
#
from collections import deque

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for a in range(1, n+1):
    tmp = list(map(int, input().split()))
    for b in range(len(tmp)):
        if tmp[b] == 1:
            if a not in graph[b+1]:
                graph[b+1].append(a)
            if b+1 not in graph[a]:
                graph[a].append(b+1)

l = list(map(int, input().split()))


def bfs(target, current, visited, graph):
    q = deque()
    visited[current] = True
    for a in range(len(graph[current])):
        q.append((graph[current][a]))
        
    while q:
        move = q.popleft()
        visited[move] = True
        
        if move == target:
            return True
        
        for a in range(len(graph[move])):
            q.append(graph[move][a])
    return False

for a in range(len(l)-1):
    target = l[a+1]
    current = l[a]
    visited = [False]*(len(l)+1)
    temp = []
    if bfs(target, current, visited, graph):
        pass
    else:
        print("NO")
        break
    if a  == len(l)-2:
        print("YES")
        
        
        
        
        
# from collections import deque

# n = int(input())
# m = int(input())
# graph = [[] for _ in range(n+1)]

# for a in range(1, n+1):
#     tmp = list(map(int, input().split()))
#     for b in range(len(tmp)):
#         if tmp[b] == 1:
#             if a not in graph[b+1]:
#                 graph[b+1].append(a)
#             if b+1 not in graph[a]:
#                 graph[a].append(b+1)

# l = list(map(int, input().split()))

# def dfs(target, current, visited, graph, temp):
#     visited[current] = True
#     print(visited, current)
#     if current == target:
#         print(0)
#         temp.append(True)
#         return temp
    
#     for a in range(len(graph[current])):
#         if visited[graph[current][a]] != True:
#             visited[graph[current][a]] = True
#             dfs(target, graph[current][a], visited, graph,temp)


# for a in range(len(l)-1):
#     target = l[a+1]
#     current = l[a]
#     visited = [False]*(len(l)+1)
#     temp = []
    
#     print(dfs(target, current, visited, graph, temp))
    
#     # if check == True:
#     #     pass
#     # else:
#     #     print("NO")
#     #     break
    
#     if a  == len(l)-2:
#         print("YES")
    



