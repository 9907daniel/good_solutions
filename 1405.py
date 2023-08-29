# 15:02
# 
# 문제 풀이 : 우선 WSNE를 갈 모든 경우의 수들을 구하자
# -> 4*4*4*4*4*...14번 -> 3천만
# 
# 
# 
# 
# 

possible = ['E','W','S','N']
movements = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

n,i,j,k,o = map(int, input().split())
percentage = [i,j,k,o]

answer = 0
tmp_value = 1
def combinations(x,y, visited, steps):
    global answer
    global tmp_value
    visited[x][y] = True
    
    if steps == n:
        answer += tmp_value
        return
    
    for a in range(4):
        nx = dx[a]+x
        ny = dy[a]+y
        if visited[nx][ny] != True and percentage[a] != 0:
            visited[nx][ny] = True
            tmp_value = tmp_value*(percentage[a]/100)
            combinations(nx,ny,visited, steps+1)
            tmp_value = tmp_value/(percentage[a]/100)
            visited[nx][ny] = False
visited = [[False]*(2*n+1) for _ in range(2*n+1)]

start = n

combinations(n,n, visited, 0)
print(answer)
    
# 전체 확률..? 
# 4*4 = 16
# 0.5 * 12 = 6
#
# 12 / 16 -> 0.75
#
# 
#
#
#



