#
# 09:13
#
# 구현할꺼
# 1) 벽 내구도 검사 (각 라운드마다 -1씩)
# 0) 이동할수 있을지 여부
# 2) 이동경로 (최단거리 + 지켜야 하는 규칙) - CLEAR
#   - BFS 를 통해 참여자 -> 출구가 아니라 출구 -> 모든 지점까지의 최속값을 찾자
#   - 다중 일떄.. -> 찾을때 + 상하 vs 왼오 판별 더 쉽다
# 0) 회전할 정사각형을 구하기
# 3) 회전 (특정 정사각형만)
# 4) 게입 끝 조건 확인
#
from collections import deque

n,m,k = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))


participants = []
for _ in range(m):
    tmp_participatns = list(map(int, input().split()))
    participants.append([a-1 for a in tmp_participatns])

tmp_x, tmp_y = map(int, input().split())
exit_x, exit_y = tmp_x-1,tmp_y-1
graph[exit_x][exit_y] = -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]

step_count = 0


def bfs(x,y,visited,graph,coordinates, distance, count):
    q = deque()
    q.append((x,y, count))
    visited[x][y]= True

    while q:
        i,j,steps = q.popleft()
        distance[i][j] = steps

        for a in range(4):
            nx = dx[a] + i
            ny = dy[a] + j

            if 0<=nx<n and 0<=ny<n and visited[nx][ny] == False:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny, steps+1))
    return distance

def find_square(participants, exit_x, exit_y):
    squared_distance_max = int(1e8)
    for a in participants:
        o = abs(a[0]-exit_x)
        p = abs(a[1]-exit_y)
        decided = max(o,p)
        squared_distance_max = min(decided, int(squared_distance_max))
    if squared_distance_max != int(1e8):
        for a in range(n-squared_distance_max):
            for b in range(n-squared_distance_max):
                # 안에 포함되어 있다면
                if a<= exit_x <= a+squared_distance_max and b<= exit_y <=b+squared_distance_max:
                    split_graph = []
                    for c in range(a, a+squared_distance_max+1):
                        sg = []
                        for d in range(b, b+ squared_distance_max+1):
                            sg.append(graph[c][d])
                        split_graph.append(sg)
    return split_graph, [a,a+squared_distance_max,b,b+squared_distance_max]

def people_find_square(participants, people_location, square, coordinates):
    split_graph = []
    for c in range(coordinates[0], coordinates[0]+len(square)):
        sg = []
        for d in range(coordinates[0], coordinates[0]+len(square)):
            sg.append(people_location[c][d])
        split_graph.append(sg)
    return split_graph



def rotate_with_zip(matrix, angle = 90):
    arr = list(map(list, zip(*matrix[::-1])))   # 시계 방향
    return arr

def rotate_with_zip_people(matrix, angle = 90):
    arr = list(map(list, zip(*matrix[::-1])))   # 시계 방향
    tmp = []
    for a in range(len(matrix)):
        for b in range(len(matrix)):
            if arr[a][b] == True:
                tmp.append([a,b])
    return arr,tmp

def break_wall(rotated, graph, coordinates,people_square, people_location):
    for a in range(len(rotated)):
        for b in range(len(rotated)):
            if rotated[a][b] != 0:
                graph[coordinates[0]+a][coordinates[2]+b] = rotated[a][b]-1
                if rotated[a][b] < 0:
                    exit_x, exit_y = coordinates[0]+a, coordinates[2]+b
            else:
                graph[coordinates[0]+a][coordinates[2]+b] = 0
            if people_square[a][b] != False or people_square[a][b] == 0:
                people_location[coordinates[0]+a][coordinates[2]+b] = people_square[a][b]
            else:
                people_location[coordinates[0]+a][coordinates[2]+b] = False

    return graph, people_location, exit_x, exit_y

def people_graph(people_location, participants):
    for a in participants:
        people_location[a[0]][a[1]] = True
    return people_location

def move(participants, distancee, exit_x, exit_y):
    global step_count
    for a in range(len(participants)-1,-1,-1):
        requirement_distance = abs(exit_x-participants[a][0]) + abs(exit_y-participants[a][1])

        current_person_x = participants[a][0]
        current_person_y = participants[a][1]

        current_person_max = 1e8
        current_direction = 9
        for b in range(4):
            nx = dx[b]+current_person_x
            ny = dy[b]+current_person_y

            if 0<=nx<n and 0<=ny<n and distance[nx][ny] != 1e8:
                if distance[nx][ny] < current_person_max:
                    current_person_max = distance[nx][ny]
                    current_direction = b
                elif distance[nx][ny] == current_person_max:
                    if b < current_direction:
                        current_direction = b

        if current_person_max != 1e8 and current_person_max < requirement_distance:
            participants[a][0] = participants[a][0] + dx[current_direction] 
            participants[a][1] = participants[a][1] + dy[current_direction] 
            step_count += 1

        if graph[participants[a][0]][participants[a][1]] < 0:
            participants.pop(a)
    return participants

while k > 0:
    k -= 1
    visited = [[False]*n for _ in range(n)]
    people_location = [[False]*n for _ in range(n)]
    distance = [[1e8]*n for _ in range(n)]

    people_location[exit_x][exit_y] = 0

    # 사람들 어디있는지 표에다 표시
    people_location = people_graph(people_location, participants)

    # 각 인원까지의 최솟값
    distance_calculated = bfs(exit_x, exit_y, visited, graph, participants, distance, 0)

    # 이동하고 삭제하기
    participants = move(participants, distance, exit_x, exit_y)

    # 회전 정사각형 좌표 찾기
    square, coordinates = find_square(participants, exit_x, exit_y)

    # 실제로 회정하기
    rotated = rotate_with_zip(square)

    # 인간들 회전 정사각형 좌표 찾기
    people_square = people_find_square(participants, people_location, square, coordinates)

    # 사람들도 회전하기
    people_square, rotated_people_square = rotate_with_zip_people(people_square)

    # 회전한 정사각형 총 그래프에 적용 + 벽 체력 삭감
    graph, people_location, exit_x, exit_y = break_wall(rotated, graph, coordinates, people_square, people_location)
    print(exit_x, exit_y)
    if len(participants) == 0:
        break

# print(graph)
# print(participants)
# print(people_location)
# # print(step_count, exit_x+1, exit_y+1)

[[0, 8, 0, 0, 1],
[0, 1, 0, 0, 0], 
[-2, 1, 0, 1, 0], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0]]


[[0, 8, 0, 0, 1], 
[0, 0, 0, 0, 0], 
[-2, 0, 0, 1, 0], 
[0, 0, 0, 1, 0], 
[0, 0, 0, 0, 0]]


[[0, 8, 0, 0, 1], 
[0, 0, 0, 0, 0],
 [-2, 0, 0, 1, 0],
  [0, 0, 0, 1, 0], 
  [0, 0, 0, 0, 0]]


[[0, 8, 0, 0, 1], 
[0, 0, 0, 0, 0],
[-2, 0, 0, 1, 0],
 [0, 0, 0, 1, 0],
  [0, 0, 0, 0, 0]]


[[0, 8, 0, 0, 1], [0, 0, 0, 0, 0], [-2, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
[[0, 8, 0, 0, 1], [0, 0, 0, 0, 0], [-2, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
[[0, 8, 0, 0, 1], [0, 0, 0, 0, 0], [-2, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]
[[0, 8, 0, 0, 1], [0, 0, 0, 0, 0], [-2, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 0]]