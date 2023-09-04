# 09:04 ~ 
# 
# 
# <문제> 
# 1) 현재 위치에서 가장 가까운 승객을 구한다
# 2) 데리로 가고, 목적지까지 내려다 준다
# 3) 재충전하고 다음 사람을 채운다 
# 
# ** 연료 과리가 중요하다
# 
# <풀이법>
# 1) 어차피 최악의 상황을 고려해야하니.. 차라리 처음부터 모든 좌표에서의 모든 이동거리를 구해서
# 3차원 배열에 관리를 하면 시간복잠도가 얼마나 될까.
# 20*20*20
# -> 오히려 매번 구해주는것보다 쉬울수 있다
#  
# 
from collections import deque
import sys

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(i,j, steps, graph):
    visited = [[False]*n for _ in range(n)]
    count = [[-1]*n for _ in range(n)]
    
    q = deque()
    q.append((i,j,steps))
    visited[i][j] = True
    
    while q:
        x,y, current_steps = q.popleft()    
        count[x][y] = current_steps    
        for a in range(4):
            nx = dx[a] + x
            ny = dy[a] + y
            
            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if visited[nx][ny] != True and graph[nx][ny] != 1:
                    visited[nx][ny] = True
                    q.append((nx,ny,current_steps+1))
                    
    return count
        
n, m, fuel = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

xx,yy = map(int, input().split())
taxi_current_x, taxi_current_y = xx-1, yy-1


orders = []
for _ in range(m):
    oo = list(map(int, input().split()))
    orders.append([oo[0]-1,oo[1]-1,oo[2]-1,oo[3]-1])

all_possible = [[0]*n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if graph[a][b] != 1:
            tmp = bfs(a,b, 0, graph)
            all_possible[a][b] = tmp
print(all_possible)

customers_visited = [False]*len(orders)

steps = 0
while steps < m:
    current_graph = all_possible[taxi_current_x][taxi_current_y]

    min_x, min_y = 1e8,1e8
    min_total_distance = 1e8
    current_minimum = []
    remove_index = 0
    for a in range(len(orders)):
        if customers_visited[a] != True:
            customer_start_x,customer_start_y = orders[a][0],orders[a][1]
            customer_end_x, customer_end_y = orders[a][2],orders[a][3]
            
            if current_graph[customer_start_x][customer_start_y] == -1 or current_graph[customer_end_x][customer_end_y] == -1:
                fuel = -1
                break
            
            if current_graph[customer_start_x][customer_start_y] != min_total_distance:   
                if current_graph[customer_start_x][customer_start_y] < min_total_distance:
                    min_total_distance = current_graph[customer_start_x][customer_start_y]
                    min_x, min_y = customer_start_x, customer_start_y
                    current_minimum = orders[a]
                    remove_index = a
            elif customer_start_x <= min_x:
                if customer_start_x == min_x:
                    if customer_start_y < min_y:
                        min_total_distance = current_graph[customer_start_x][customer_start_y]
                        min_x, min_y = customer_start_x, customer_start_y
                        current_minimum = orders[a]
                        remove_index = a
                else:
                    min_total_distance = current_graph[customer_start_x][customer_start_y]
                    min_x, min_y = customer_start_x, customer_start_y
                    current_minimum = orders[a]
                    remove_index = a
    customers_visited[remove_index] = True
    steps += 1

    if len(current_minimum) == 0:
        break
    
    print(current_graph)
    
    destination_graph = all_possible[current_minimum[0]][current_minimum[1]]
    
    print(destination_graph)
    
    
    if current_graph[current_minimum[0]][current_minimum[1]] + destination_graph[current_minimum[2]][current_minimum[3]] <= fuel:
        taxi_current_x = current_minimum[2]
        taxi_current_y = current_minimum[3]
        fuel -= current_graph[current_minimum[0]][current_minimum[1]] + destination_graph[current_minimum[2]][current_minimum[3]]
        fuel += (destination_graph[current_minimum[2]][current_minimum[3]])*2
    else:
        fuel = -1
        break


if False  n customers_visited:
    print(-1)
else:
    print(fuel)
    
# [[11, 10, -1, 8, 7, 6],
#  [10, 9, -1, 7, 6, 5], 
#  [9, 8, 7, 6, 5, 4], 
#  [8, 7, 6, 5, 4, 3], 
#  [9, 8, 7, 6, -1, 2], 
#  [10, 9, 8, -1, 0, 1]]

# [[7, 6, -1, 4, 5, 6], 
#  [6, 5, -1, 3, 4, 5], 
#  [5, 4, 3, 2, 3, 4],
#  [4, 3, 2, 1, 2, 3], 
#  [3, 2, 1, 0, -1, 4],
#  [4, 3, 2, -1, 6, 5]]