# 양방향 최적거리 (다이엑스트라)

import heapq

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [1e8]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    
    graph[a].append([b,1])
    graph[b].append([a,1])
    
k,x = map(int, input().split())

def dijikstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    # q[0] = current_location
    # q[1] = distance
    distance[start] = 0
    
    while q:
        current_node, current_distance = heapq.heappop(q)
        
        if distance[current_node] < current_distance:
            continue
        
        for a in graph[current_node]:
            sum_distance = current_distance + a[1]
            
            if sum_distance < distance[a[0]]:
                distance[a[0]] = sum_distance
                heapq.heappush(q, (a[0],sum_distance))
                
sum = 0
dijikstra(x)
sum += distance[k]
distance = [1e8]*(n+1)
dijikstra(k)
sum += distance[x]+1

if sum >= 1e8:
    print(-1)
else:
    print(sum)