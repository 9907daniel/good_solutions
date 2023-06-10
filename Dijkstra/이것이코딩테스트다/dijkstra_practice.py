# n, m = 6, 11

# start = 1
# 1 2 2 : 1->2 cost = 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
import heapq

n,m = map(int, input().split())
start = int(input())
distance = [1e8]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    # b : destination
    # c : cost

def dijikstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    distance[start] = 0
    
    while q:
        current_node, current_distance = heapq.heappop(q)
        
        if distance[current_node] < current_distance:
            continue
        
        for a in graph[current_node]:
            sum_distance = current_distance + a[1]
            if sum_distance < distance[a[0]]:
                distance[a[0]] = sum_distance
                heapq.heappush(q, (a[0], sum_distance))
        
dijikstra(start)


for i in range(1, n+1):
    if distance[i] ==  1e8:
        print(1e8)
    else:
        print(distance[i])



# n,m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n+1)]
# distance = [1e8]*(n+1)

# for _ in range(m):
#     a,b,c = map(int, input().split())
    
#     graph[a].append([b,c])
    
#     # b : destination
#     # c : cost
    

# def dijikstra(start):
#     q = []
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
    
#     while q:
#         current_dist, current_node = heapq.heappop(q)
        
#         if distance[current_node] < current_dist:
#             continue
        
#         for a in graph[current_node]:
#             added_distance = current_dist + a[1]
            
#             if distance[a[0]] > added_distance:
#                 distance[current_node] = added_distance
#                 heapq.heappush(q, (added_distance, a[0]))

# dijikstra(start)
# print(distance)