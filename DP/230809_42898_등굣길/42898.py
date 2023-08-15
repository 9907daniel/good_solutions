# 09:09 ~ 09:31 + 10:27 ~ 10:56
#
# BFS / DFS 풀이를 해도 괜찮을꺼 같은데.. 효율성 테스트 떄문에 주어진 DP로..
#
# -> 100! 이기 때문이 TLE
#

def solution(m, n, puddles):    
    dp = [[0]*m for _ in range(n)]
    
    track = [[False]*m for _ in range(n)]
    if puddles[0] != []:
        for a in puddles:
            track[a[1]-1][a[0]-1] = True
        
    dp[0][0] = 1
    for a in range(n):
        for b in range(m):
            if track[a][b] != True:
                if 0<= a-1 and 0<= b-1 and track[a-1][b] == False and track[a][b-1] == False:      
                    dp[a][b] = dp[a-1][b] + dp[a][b-1]
                elif 0<= a-1 and track[a-1][b] == False:
                    dp[a][b] = dp[a-1][b]    
                elif 0<= b-1 and track[a][b-1] == False:
                    dp[a][b] = dp[a][b-1] 
                
    
    return (dp[n-1][m-1]) % 1000000007
    

################## 풀이 1)
# dx = [1,0]
# dy = [0,1]
# count = 0
# def dfs(graph, x, y, track, m, n):
#     global count
#     if x == n-1 and y == m-1:
#         count += 1
#         return
#     for a in range(2):
#         nx = dx[a] + x
#         ny = dy[a] + y
#         if nx <= n-1 and ny <= m-1 and track[nx][ny] != True:
#             dfs(graph, nx,ny, track, m, n)
#     return
# def solution(m, n, puddles):
#     graph = [[0]*m for _ in range(n)]
#     track = [[False]*m for _ in range(n)]
#     if puddles[0] != []:
#         for a in puddles:
#             track[a[1]-1][a[0]-1] = True
#     dfs(graph, 0, 0, track, m,n)
#     return count
    
    

################## 풀이 2)
# def solution(m, n, puddles):
#     # DP를 이중으로 만들어 X[0] = 현재 steps, X[1] = 현재 Steps 겹치는 경로 개수
#     dp = [[[0,1] for _ in range(m)] for _ in range(n)]
#     # 물 잠김 기록
#     track = [[False]*m for _ in range(n)]   
#     if puddles[0] != []:
#         for a in puddles:
#             track[a[1]-1][a[0]-1] = True   
#     print(track)
#     for a in range(n):
#         for b in range(m):
#             # 만약 현재 위치가 물에 잠기지 않았다면..
#             if track[a][b] != True:       
#                 # 만약 위 아래 둘다 물에 잠기지 않았다면 ..
#                 if 0<= a-1 and 0<= b-1 and track[a-1][b] == False and track[a][b-1] == False:              
#                     # 그리고 둘다 막혀있지 않다면! 
#                     if dp[a-1][b][0] == 0 and dp[a][b-1][0] == 0:
#                         dp[a][b][0] = 0       
#                     # 막혀 있지 않다면 위,아래 최소 스탭 중에 +1
#                     else:
#                         dp[a][b][0] = min(dp[a-1][b][0], dp[a][b-1][0]) + 1              
#                     # 경로 갱신 위아래 같다면 둘다 더해줄수 있다
#                     if dp[a-1][b][0] == dp[a][b-1][0]:
#                         dp[a][b][1] = dp[a-1][b][1] + dp[a][b-1][1]               
#                     elif dp[a-1][b][0] < dp[a][b-1][0]:
#                         dp[a][b][1] = dp[a-1][b][1]     
#                     elif dp[a-1][b][0] > dp[a][b-1][0]:
#                         dp[a][b][1] = dp[a][b-1][1]
#                 # 위만 가능
#                 elif 0<= a-1 and track[a-1][b] == False:
#                     if dp[a-1][b][0] == 0 and a-1 != 0:
#                         dp[a][b][0] = dp[a-1][b][0]
#                     else:
#                         dp[a][b][0] = dp[a-1][b][0] + 1
#                     dp[a][b][1] = dp[a-1][b][1]   
#                 # 옆만 가능
#                 elif 0<= b-1 and track[a][b-1] == False:
#                     if dp[a][b-1][0] == 0 and b-1 != 0:
#                         dp[a][b][0] = dp[a][b-1][0]
#                     else:
#                         dp[a][b][0] = dp[a][b-1][0] + 1
#                     dp[a][b][1] = dp[a][b-1][1]
#                 if dp[a][b][0] == 0 and a != 0 and b != 0:
#                     dp[a][b][1] = 0
#     return (dp[n-1][m-1][1]) % 1000000007
    
    
    
    