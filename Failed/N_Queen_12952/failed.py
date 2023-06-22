# 12*12*12!
#
# 완탐, DFS/BFS, maybe 조합
#
# 옆줄, 앞줄, 대각선에 서로 배치가 되어 있으면 안된다
#
# 틀린 풀이
# 1. 시작 지점을 정하는 for 가로, for 세로
# 2. 탐색 시작하고, 배치 되어 있는 Q에서 모두 visited처리 
#
# 틀림
# 1. 모든 Q가 다른 가로와 다른 세로에 들어 있다면 통과


from itertools import permutations

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]

def checkout(l, n):
    visited = [[False]*n for _ in range(n)]
    
    for a in l:
        x = a[0]
        y = a[1]
        for i in range(8):
            nx = dx[i]+x
            ny = dy[i]+y

            while 0<=nx<n and 0<=ny<n:
                nx = dx[i]+nx
                ny = dy[i]+ny

                if visited[nx][ny] == True:
                    return False
                else:
                    x = nx
                    y = ny
                    visited[nx][ny] = True
            x = a[0]
            y = a[1]
    return True
    

def solution(n):
    l = [a for a in range(n)]
    results = []
    for a in range(n):
        for b in range(n):
            results.append([a,b])
            
    count = 0    
    for a in permutations(results, n):
        if checkout(a, n):
            count += 1
            
    
    