# 15:22 ~ 15:47
#
# 그냥 완전탐색 DFS / BFS를 사용하면 된다
#
# BFS도 가능할뜻한데.. 방문처리를 중복으로 해야해서 복잡해진다
# 그냥 DFS를 사용하자
#

r,c,k = map(int, input().split())


dx = [-1,1,0,0]
dy = [0,0,-1,1]

graph = []
for _ in range(r):
    graph.append(list(input()))
    
visited = [[False]*c for _ in range(r)]

answer = 0
def dfs(graph, visited, count, x,y):
    global answer
    visited[x][y] = True
    
    if x == 0 and y == c-1:
        if count == k:
            answer += 1
        return
    
    for a in range(4):
        nx = dx[a]+x
        ny = dy[a]+y
        if 0<=nx<r and 0<=ny<c:
            if visited[nx][ny] != True and graph[nx][ny] != 'T':
                visited[nx][ny] = True
                dfs(graph, visited, count+1, nx,ny)
                visited[nx][ny] = False


dfs(graph, visited, 1, r-1, 0)
print(answer)


