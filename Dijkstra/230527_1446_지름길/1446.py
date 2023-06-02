import heapq

n,d = map(int, input().split())

graph = [[] for _ in range(d+1)]
# distance = [a for a in range(d+1)] # [0,1,2,3,4,....]
distance = [1e8]*(d+1)

for a in range(n):
    i,j,x = map(int, input().split())
    graph[i] = (j,x) # to-node, cost
    
def dijikstra(start):
    q = []
    heapq.heappush(q, [0,start])
    
    while q:
        current, cost = heapq.heappop(q)
        if d[current] < cost:
            continue
            # if distance[now] < dist:
            #     continue
        for a in graph[current]:
            total = cost + a[1]
            if total < distance[a[0]]:
                distance[a[0]] = total
                heapq.heappush(q, [total,a[0]])

dijikstra(0)

print(distance)



