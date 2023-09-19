
from heapq import heappush, heappop

n,m,k,x = map(int, input().split())

# 필요한거는 : distance, visited, graph
distance = [1e8]*(n+1)
visited = [False]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append((b,1)) # a->b 까지 값 1
    
def dijikstra(start):
    q = []
    heappush(q, (start, 0))
    distance[start] = 0
    
    while q:
        current_node, dist = heappop(q)
        
        if distance[current_node] < dist:
            continue
        
        for a in graph[current_node]:
            summed_dist = dist + 1
            if summed_dist < distance[a[0]]:
                heappush(q, (a[0], summed_dist))
                distance[a[0]] = summed_dist
        
dijikstra(x) 

if k not in distance:
    print(-1)
else:
    for a in range(len(distance)):
        if distance[a] == k:
            print(a)

# answer = []
# for a in range(len(distance)):
#     if distance[a] == k:
#         answer.append(a)

# if len(answer) == 0:
#     print(-1)
# else:
#     for a in answer:
#         print(a)








