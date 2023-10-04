# 21:16 ~ 21:28
#
# 뮨제는 복잡하지만.. 그냥 모든 간선을 그리고, 다익스트라를 통해 최소 거리를 구한다면..
# 그것이 최소 값이 맞지 않을까..?
#
#

from heapq import heappush,heappop

n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]
distance = [1e8]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) 
    graph[b].append((a,c)) # b->a 까지 가는데 c가 든다
    
s,t = map(int, input().split())


def dijikstra(start):
    q = []
    distance[start] = 0 # 거리를 0으로 초기화
    # visited[start] = True
    heappush(q, (start, 0)) # 위치, 거리 추가
    
    while q:
        current_node, current_distance = heappop(q)
        
        if distance[current_node] < current_distance:
            continue
        
        for b in graph[current_node]:
            summed_distance = current_distance+b[1]
            
            if summed_distance < distance[b[0]]:
                distance[b[0]] = summed_distance
                heappush(q, (b[0], summed_distance))

dijikstra(s)
print(distance[t])





