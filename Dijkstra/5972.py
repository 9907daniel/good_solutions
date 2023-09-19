# 09:34 ~ 09:43

from heapq import heappush, heappop

n,m = map(int, input().split())

distance = [1e8]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a->b 는 c비용
    graph[b].append((a,c))

def dijikstra(start):
    q = []
    heappush(q,(start, 0))
    distance[start] = 0
    
    while q:
        current_node, cost = heappop(q)
        
        if distance[current_node] < cost:
            continue
        
        for a in graph[current_node]:
            summed_cost = cost + a[1]
            
            if summed_cost < distance[a[0]]:
                heappush(q, (a[0], summed_cost))
                distance[a[0]] = summed_cost

dijikstra(1)

print(distance[n])




