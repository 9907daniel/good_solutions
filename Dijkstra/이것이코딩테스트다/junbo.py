import heapq
n,m,c = map(int, input().split())
graph = [[]for _ in range(n+1)]
distance = [1e8]*(n+1)

for _ in range(m):
    x,y,z = map(int, input().split())
    
    graph[x].append([y,z])
                    # y = destination, z = cost
                    
def dijikstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    
    while q:
        current_node, current_distance = heapq.heappop(q)
    
        # 이미 최소값이다 -> 할 필요 없다
        if distance[current_node] < current_distance:
            continue
        
        for a in graph[current_node]:
            sum_distance = a[1] + current_distance
            if sum_distance < distance[a[0]]:
                distance[a[0]] = sum_distance
                heapq.heappush(q, (a[0], sum_distance))
    
dijikstra(c)

count = 0
current_max = 0
for a in range(len(distance)):
    if distance[a] != 1e8:
        count += 1
        current_max = max(current_max, distance[a])
        
print(count-1, current_max)