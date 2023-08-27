# 09:09 ~ 09:50
# 
# 2x2 칸이 있다
# 50 30
# 20 40
# 
# <설계>
# 1) 전체 bfs를 통해 안구차를 구하여 섬의 갯수들(연습의 갯수들을 구한다)
#  1-1) 조건문 = 인구차
# 2) 각 섬들에 대해 N분을 해준다
# 
# 
# 3 5 10
# 10 15 20
# 20 30 25
# 40 22 10
# 
# 10 15 20 
# 20 30 25
#    22    + 40 + 10
# 
# 
# 이 상황에서는 bfs vs dfs일까? -> bfs가 최적일듯
#
# 반례)
# 오히려 시간제한이 걸린다..? -> DFS했으면 TLE 걸렸을 확률이 있다
#

from collections import deque
from copy import deepcopy

n,l,r = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


def bfs(graph, visited, x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    tmp =[[x,y]] 
    
    while q:
        i,j = q.popleft()
        
        for a in range(4):
            nx = dx[a] + i
            ny = dy[a] + j
            
            if 0<=nx<n and 0<=ny<n:
                # 평범한 BFS 지만 국가간 차이가 밤위안에 든다면.. 을 조건으로 단다
                if visited[nx][ny] != True and l<= abs(graph[i][j]-graph[nx][ny])<=r:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    tmp.append([nx,ny])
                    
    return tmp, visited

def spread(graph, coordinates):
    # 한 연합군씩 iterate
    for a in range(len(coordinates)):
        average_population = 0
        # 현재 연합군 sum 구하기
        for b in range(len(coordinates[a])):
            average_population += graph[coordinates[a][b][0]][coordinates[a][b][1]]
        # 연합군의 국가 수만큼 나눠주기
        average_population = average_population//len(coordinates[a])
        
        # BFS때 기록해준 좌표를 활용해 spread
        for b in range(len(coordinates[a])):
            graph[coordinates[a][b][0]][coordinates[a][b][1]] = average_population
    return graph
    

count = 0
while True:
    # 인구 이동이 끝나는 회차는, 그래프의 전과 후가 동일할때이다
    before_changes = deepcopy(graph)
    
    coordinates = []
    visited = [[False]*n for _ in range(n)]
    
    # 모든 섬들의(연합) 국경선을 구해주는것이기 때문에 전체 탐색을 한다
    for a in range(n):
        for b in range(n):
            if visited[a][b] != True:
                # 매번 돌려받는 새 연합군의 좌표들을 coordiantes에 관리해준다 
                # 예시)
                # Coordaintes = 
                # 0,0 0,1, 1,0, 1,1, 0,2, 2,1 1,2
                # 0 2
                # 2 2
                new_alliance, visited = bfs(graph, visited, a,b)
                coordinates.append(new_alliance)
    # 전체 연합군들을 구한다면 평균화를 시켜준다
    graph = spread(graph, coordinates)
    
    # 비교는 전과 후를 비교했을때 변화가 있었는지다    
    if before_changes == graph:
        break
    else:
        # 동일하지 않다면 비교
        count += 1

print(count)








