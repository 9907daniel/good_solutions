
from heapq import heappush, heappop

n,m = map(int, input().split())

graph = [[] for _ in range(n+1)]
distance = [1e8]*(n+1)
visited = [False]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split()) # a->b 는 c만큼 든다
    graph[a].append((b,c)) # 목적지, 값
    graph[b].append((a,c))
    

def dijikstra(start):
    q = []
    heappush(q, (start, 0)) # 시작점, 값
    distance[start] = 0
    
    while q:
        current_node, dist = heappop(q) # 0,0
        
        if distance[current_node] < dist:
            continue
        
        for a in graph[current_node]:
            summed_distance = dist + a[1]
            if summed_distance < distance[a[0]]:
                distance[a[0]] = summed_distance
                heappush(q, (a[0], summed_distance))

    
dijikstra(0)