# 09:16 ~ 10:32
# 
# R+G -> 10
# 배양액 -> 1~5,1~5
# --> 10*9 / 10! -> 10!의 조합이 올 수 있다 
#  
# -> 퍼트리는거는 BFS가 좋을꺼 같다
# 
# 

from collections import deque

n,m,g,r = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

startable = []

for a in range(n):
    for b in range(m):
        if graph[a][b] == 2:
            startable.append([a,b])

total = []
greens = []
reds = []
def backtrack(startable, current, visited):
    if current == r+g:
        if len(greens) == g and len(reds) == r:
            total.append(greens+reds)
        return 
    
    for a in range(current, len(startable)):
        if visited[startable[a][0]][startable[a][1]] != True:
            g_coord = ["g",startable[a][0], startable[a][1]]
            visited[startable[a][0]][startable[a][1]] = True
            greens.append(g_coord)
            backtrack(startable, current + 1, visited)
            greens.pop()
            
            r_coord = ["r",startable[a][0], startable[a][1]]
            reds.append(r_coord)
            backtrack(startable, current +1, visited)
            reds.pop()
            visited[startable[a][0]][startable[a][1]] = False
    return

dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = 0
    
def bfs(board,graph,total, spread):
    global answer
    q = deque()
    for a in range(len(total)):
        q.append((total[a],0))

    current_answer = 0
        
    while q:
        current_flower, count = q.popleft()

        for j in range(4):
            nx = current_flower[1]+dx[j]
            ny = current_flower[2]+dy[j]
                        
            if 0<=nx<n and 0<=ny<m:
                if board[nx][ny] != 'G' and board[nx][ny] != 'R' and board[nx][ny] != 'F' and graph[nx][ny] != 0:
                    if spread[nx][ny] == []:
                        if current_flower[0] == 'g':
                            spread[nx][ny] = ['g', count]
                            q.append((["g",nx, ny], count+1))
                            
                        elif current_flower[0] == 'r':
                            spread[nx][ny] = ['r', count]
                            q.append((["r",nx, ny], count+1))

                    elif current_flower[0] == 'g' and spread[nx][ny][0] == 'r' and spread[nx][ny][1] == count:
                        board[nx][ny] = 'F'
                        current_answer += 1
                    elif current_flower[0] == 'r' and spread[nx][ny][0] == 'g' and spread[nx][ny][1] == count:
                        board[nx][ny] = 'F'
                        current_answer += 1   
    answer = max(answer, current_answer)

visited = [[False]*m for _ in range(n)]
backtrack(startable, 0, visited)

for a in range(len(total)):
    board = [["-"]*m for _ in range(n)]
    spread = [[[] for _ in range(m)] for _ in range(n)]

    # print(total[a])
    for b in range(len(total[a])):
        if total[a][b][0] == 'g':
            board[total[a][b][1]][total[a][b][2]] = "G"
        else:
            board[total[a][b][1]][total[a][b][2]] = "R"
    
    bfs(board,graph,total[a], spread)

print(answer)