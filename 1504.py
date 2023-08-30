# 14:08
#
#
# 노드를 지나야하니.. 그 노드가 포함되어 있을때만 최신화를 하면 가능 할꺼 같다
# 
# 
# 
# 
# 
# 
# 

import heapq
from copy import deepcopy

n,e = map(int, input().split())

graph = [[] for _ in range(n+1)]


distance = [1e8]*(n+1)
visited = [False]*(n+1)

for _ in range(e):
    a,b, cost = map(int, input().split())
    graph[a].append((b, cost))
    graph[b].append((a, cost))
checkpoint_1, checkpoint_2 = map(int, input().split())


def dijikstra(start, target):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    
    while q:
        current_distance, current_node = heapq.heappop(q)
        
        if distance[current_node] < current_distance:
            if current_node == target:
                return 
            continue
        
        for a in graph[current_node]:
            added_distance = a[1] +  current_distance
            
            if added_distance < distance[a[0]]:
                visited[a[0]] = True
                distance[a[0]] = added_distance
                heapq.heappush(q, (added_distance, a[0]))                

# tmp = []
# dijikstra(1, tmp)


#################
visited = [False]*(n+1)
distance = [1e8]*(n+1)
dijikstra(1)
tmp_1 = deepcopy(distance)
mid = tmp_1[checkpoint_1]

distance = [1e8]*(n+1)
dijikstra(checkpoint_1, checkpoint_2)
tmp_2 = deepcopy(distance)
mid_2 = tmp_2[checkpoint_2]

if visited[checkpoint_2] == True:
    first = mid+mid_2
else:
    distance = [1e8]*(n+1)
    dijikstra(checkpoint_2)
    end = distance[-1]
    first = end+mid+mid_2
# #####################

distance = [1e8]*(n+1)
dijikstra(1)
tmp_3 = deepcopy(distance)
mid3 = tmp_3[checkpoint_2]

visited = [False]*(n+1)
distance = [1e8]*(n+1)
dijikstra(checkpoint_2, checkpoint_1)
tmp_4 = deepcopy(distance)
mid4 = tmp_4[checkpoint_1]

distance = [1e8]*(n+1)
dijikstra(checkpoint_1)
end2 = distance[-1]

print(min(end+mid_2+mid, end2+mid3+mid4))
print(min(end,end2))
        
# # 반례 : 이미 지나가는거에서 포함되어 잇다면
#################
visited = [False]*(n+1)
distance = [1e8]*(n+1)
dijikstra(1, -1)
tmp_1 = deepcopy(distance)
mid = tmp_1[checkpoint_1]

distance = [1e8]*(n+1)
dijikstra(checkpoint_1, checkpoint_2)
tmp_2 = deepcopy(distance)
mid_2 = tmp_2[checkpoint_2]

if visited[checkpoint_2] == True:
    first = mid+distance[-1]
else:
    distance = [1e8]*(n+1)
    dijikstra(checkpoint_2, n)
    end = distance[-1]
    first = end+mid+mid_2
# #####################

distance = [1e8]*(n+1)
dijikstra(1, -1)
tmp_3 = deepcopy(distance)
mid3 = tmp_3[checkpoint_2]

visited = [False]*(n+1)
distance = [1e8]*(n+1)
dijikstra(checkpoint_2, checkpoint_1)
tmp_4 = deepcopy(distance)
mid4 = tmp_4[checkpoint_1]


# if visited[checkpoint_1] == True:
#     second = mid3+distance[-1]
# else:
#     distance = [1e8]*(n+1)
#     dijikstra(checkpoint_1, n)
#     end2 = distance[-1]
#     second = end2+mid3+mid4

print(min(first,second))











