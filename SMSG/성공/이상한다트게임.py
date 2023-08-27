# 09:03 ~ 11:01
# 
# <문제>
#  - 4방향으로 다트가 주어진다 (크로스 모양)
#  - 주어진 명령에 따라 특정 칸을 회전시켜준다
#  - 인접한 조건들을 확인하고 인접한 수의 수가 같으면 삭제를 한다
#  - 삭제하는 수가 없다면 정규화 과정을 거친다
# 
# <참고사항>
# - 이미 끝난 값들은 -1로 관리
#
# <설계>
# 1) 다트 설계
# m이 불명화한 시점에서 이차원 배열을 통해 원을 구현하는거는 불가능하다
# -> 배열을 통해 통려줘야 한다
# 
# 2) 회전
# x,d,k가 주전진다 
# 
# for n의 범위:
#    # 만약 나눈값이 배수라면 그 인덱스에 대해서 실행을 한다
#    if a+1 % x
#        if 시계방향 
#           # k번만큼 회전
#           for range(k)
#        if 반시계방향
# return 회전된 원들 
#
#
# 3) 조건들 확인
#  i) 같은 인덱스에서 앞뒤를 비교해준다
#       - 0 인덱스이면 -1 + 1 을 비교
#       - -1이라면 전 + 0을 비교
#
# -> y축은 -1->0을 이동 할 수 있는 BFS
# -> x축은 -1->0을 이동 못하는 BFS로 구현을 하면 가능하지 않나.?
#
#
#
# <반례>
# 
# 

from collections import deque
from copy import deepcopy

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n,m,q = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

orders = []
for _ in range(q):
    orders.append(list(map(int, input().split())))

def rotate(multiplier, direction, move_amount, graph):
    # 현재 턴의 배수를 찾기 위해 모든 원판 iterate
    for a in range(n):
        # 만약 주어진 턴의 배수라면
        if (a+1)%multiplier == 0:
            # 시계 방향이라면
            if direction == 0:
                # k번만큼 회전 (ex - 2번회전)
                #  5 7 4 4
                #  4 5 7
                left, right =  graph[a][:m-move_amount], graph[a][-move_amount:]
                rotated = right + left
            # 반시계 방향이라면
            elif direction == 1:
                # 5 7 4 4 
                # 
                left, right = graph[a][:move_amount], graph[a][move_amount:]
                rotated = right + left
            graph[a] = rotated[:]
    return graph


def check_bfs(graph, visited, x, y):
    q = deque()
    # -1로 바꿔줄꺼기 떄문에 그전에 값을 기록
    q.append((x,y, graph[x][y]))
    visited[x][y] = True

    while q:
        i,j, cost = q.popleft()
        for a in range(4):
            nx = i + dx[a]
            ny = j + dy[a]

            # !!!중요 포인트 : m은 원이기 떄문에 0-> -1을 순회 할 수 있다
            if 0<=nx<n and -1<=ny<=m:
                if ny == -1:
                    ny = m-1
                elif ny == m:
                    ny = 0

                if visited[nx][ny] != True and graph[nx][ny] != -1 and graph[nx][ny] == cost:
                    q.append((nx,ny, cost))
                    visited[nx][ny] = True
                    graph[nx][ny] = -1
                    graph[i][j] = -1
    return graph, visited

for turn in range(len(orders)):
    multiplier = orders[turn][0]
    direction = orders[turn][1]
    move_amount = orders[turn][2]

    graph = rotate(multiplier, direction, move_amount, graph)
    
    # 나중에 변동이 없는지 비교를 위해 저장을 해준다
    comparison_copy = deepcopy(graph)

    visited = [[False]*m for _ in range(n)]


    for a in range(n):
        for b in range(m):
            if visited[a][b] != True and graph[a][b] != -1:
                graph, visited = check_bfs(graph, visited,a,b)
                # [X, X, 3, 4], 
                # [X, X, X, X], 
                # [X, 7, X, X], 
                # [2, 6, 3, 6]

                # [[-1, -1, 3, 4], 
                # [-1, -1, -1, -1], 
                # [-1, 7, -1, -1], 
                # [2, 6, 3, 6]]


    # 정규화 
    if graph == comparison_copy:
        average = 0
        count = 0
        for a in range(n):
            for b in range(m):
                if graph[a][b] != -1:
                    average += graph[a][b]
                    count += 1

        average = average // count
        for a in range(n):
            for b in range(m):
                # 여기서 반례 걸림! -1로 표기 해준것도 +1 더해주니 갈수록 수가 늘어났다..
                if graph[a][b] < average and graph[a][b] != -1:
                    graph[a][b] = graph[a][b] + 1
                if graph[a][b] > average:
                    graph[a][b] = graph[a][b] -1

# 최종 답
answer = 0
for a in range(n):
    for b in range(m):
        if graph[a][b] != -1:
            answer += graph[a][b]

print(answer)


# [[-1, -1, 3, 10, -1], 
# [10, 7, 6, 7, -1], 
# [7, 6, -1, -1, 9], 
# [-1, -1, 2, -1, -1], 
# [-1, 9, -1, -1, -1], 
# [-1, -1, 1, -1, -1], 
# [3, 9, 4, -1, 7]]



# 7 5 6
# 8 8 3 10 8 
# 8 10 7 6 7 
# 6 10 10 9 7 
# 4 5 2 10 4 
# 5 9 10 2 4 
# 2 1 1
# X  X 3 10 X 
# 10 7 6 7 X
# 6  X X 9 7 
# X  2 X X X
# X  9 X X X 
# X  1 6 X X
# 3  9 4 6 7 

# [-1, -1, 3, 10, -1], 
# [10, 7, 6, 7, -1], 
# [6, -1, -1, 9, 7], 
# [-1, 2, -1, -1, -1], 
# [-1, 9, -1, -1, -1], 
# [-1, 1, 6, -1, -1], 
# [3, 9, 4, 6, 7]]

# 3 1 4
# X  X 3 10 X 
# 10 7 6 7  X
# 7  6 X X  9
# X  2 X X  X
# X  9 X X  X 
# X  X 1 X  X
# 3  9 4 X  7 

#  [-1, -1, 3, 10, -1], 
#  [10, 7, 6, 7, -1],
#  [7, 6, -1, -1, 9],
#  [-1, 2, -1, -1, -1],
#  [-1, 9, -1, -1, -1],
#  [-1, -1, 1, -1, -1],
#  [3, 9, 4, -1, 7]]


# 4 0 1
# X  X 4 9 X 
# 9 6 6 6  X
# 6  6 X X  8
# X  X 3 X  X
# X  8 X X  X 
# X  X 2 X  X
# 4  8 5 X  6 

# [[0, 0, 4, 9, 0]
# , [9, 6, 6, 6, 0],
#  [6, 6, 0, 0, 8]
#   [0, 0, 3, 0, 0], 
#   [0, 8, 0, 0, 0], 
#   [0, 0, 2, 0, 0],
#    [4, 8, 5, 0, 6]]


# [[-1, -1, 3, 10, -1], 
# [10, 7, 6, 7, -1], 
# [7, 6, -1, -1, 9], 
# [-1, -1, 2, -1, -1],
#  [-1, 9, -1, -1, -1],
# [-1, -1, 1, -1, -1], 
# [3, 9, 4, -1, 7]]


# 5 1 2
# 5 1 3
# 6 0 1
# [[-1, -1, 4, 11, -1], [11, 8, 7, 8, -1], [8, 7, -1, -1, 10], [-1, -1, 3, -1, -1], [-1, -1, -1, -1, 10], [-1, -1, 2, -1, -1], [4, 10, 5, -1, 8]]
# [[-1, -1, 4, 11, -1], [11, 8, 7, 8, -1], [8, 7, -1, -1, 10], [-1, -1, 3, -1, -1], [-1, 10, -1, -1, -1], [-1, -1, 2, -1, -1], [4, 10, 5, -1, 8]]
# [[-1, -1, 5, 12, -1], [12, 9, 8, 9, -1], [9, 8, -1, -1, 11], [-1, -1, 4, -1, -1], [-1, 11, -1, -1, -1], [-1, -1, -1, 3, -1], [5, 11, 6, 0, 9]]