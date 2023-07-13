# 09:55 ~ 10:23

from heapq import heappush, heappop

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    
    graph[a].append((b,c))
    
distance = [1e8]*(v+1)
current_max = 1e8

def dijikstra(start):
    global current_max
    q = []
    heappush(q, (start, 0)) # 노드 위치, 거리값
    count = 0
    while q:
        current_node, current_distance = heappop(q)
        
        if count > 0 and start == current_node:
            current_max = min(current_max, distance[start])        
        
        if distance[current_node] < current_distance:
            continue
        
        for a in graph[current_node]:
            summed_distance = current_distance+a[1]
            
            if summed_distance < distance[a[0]]:
                distance[a[0]] = summed_distance
                heappush(q, (a[0], summed_distance))
        count += 1
    

for a in range(1, v+1):
    distance = [1e8]*(v+1)
    dijikstra(a)

if current_max != 1e8:
    print(current_max)
else:
    print(-1)