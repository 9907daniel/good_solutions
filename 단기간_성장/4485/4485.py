# 22:54 ~ 
# 
# 갈 수 있는 모든 경우의 최소값이기 때문에.. BFS가 적합하다고 생각하는데..
#
# N = 125까지 가능하다면..
# 
# 입출력이 125이고.. 테스트 케이스가 여러개이기 때문에 BFS/DFS/BackTrack = TLE
#
# 풀이 1) - DP
# 현재에서 계속 이동하며 DP를 기록하는게 좋을꺼 같다
# 
answers = []
while True:
    n = int(input())
    
    if n == 0:
        break
    
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    
    lost_money = 0
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))
    
    dp = [[1e8]*n for _ in range(n)]
    
    for a in range(n):
        for b in range(n):
            if a ==0 and b == 0:
                dp[a][b] = l[a][b]
            elif a == 0:
                if b != n-1:
                    tmp = min(dp[a][b-1], dp[a+1][b], dp[a][b+1])
                else:
                    tmp = min(dp[a][b-1], dp[a+1][b])
                dp[a][b] = l[a][b] + tmp
            elif b == 0:
                if a != n-1:
                    tmp = min(dp[a][b+1], dp[a-1][b], dp[a+1][b])
                else:
                    tmp = min(dp[a-1][b], dp[a][b+1])
                dp[a][b] = l[a][b] + tmp
            else:
                if a != n-1 and b != n-1:
                    tmp = min(dp[a][b+1], dp[a-1][b], dp[a+1][b], dp[a][b-1])
                elif a != n-1:
                    tmp = min(dp[a-1][b], dp[a+1][b], dp[a][b-1])
                elif b != n-1:
                    tmp = min(dp[a-1][b], dp[a][b+1], dp[a][b-1])
                else:
                    tmp = min(dp[a-1][b], dp[a][b-1])
                dp[a][b] = l[a][b] + tmp  
            
            for c in range(4):
                nx = dx[c] + a
                ny = dy[c] + b
                print(a,b, nx,ny)
                
                if 0<=nx<n and 0<=ny<n:
                    print(l[nx][ny],dp[a][b])
                    # print(dp[nx][ny], l[nx][ny]+dp[a][b])
                    dp[nx][ny] = min(dp[nx][ny], l[nx][ny]+dp[a][b])
                
                          
    print(dp)
    answers.append(dp[n-1][n-1]) 
    
    
    
    
    
    
    
    
    # for a in range(n):
    #     for b in range(n):
    #         if a ==0 and b == 0:
    #             dp[a][b] = l[a][b]
    #         elif a == 0:
    #             if b != n-1:
    #                 tmp = min(dp[a][b-1], dp[a+1][b], dp[a][b+1])
    #             else:
    #                 tmp = min(dp[a][b-1], dp[a+1][b])
    #             dp[a][b] = l[a][b] + tmp
    #         elif b == 0:
    #             if a != n-1:
    #                 tmp = min(dp[a][b+1], dp[a-1][b], dp[a+1][b])
    #             else:
    #                 tmp = min(dp[a-1][b], dp[a][b+1])
    #             dp[a][b] = l[a][b] + tmp
    #         else:
    #             if a != n-1 and b != n-1:
    #                 tmp = min(dp[a][b+1], dp[a-1][b], dp[a+1][b], dp[a][b-1])
    #             elif a != n-1:
    #                 tmp = min(dp[a-1][b], dp[a+1][b], dp[a][b-1])
    #             elif b != n-1:
    #                 tmp = min(dp[a-1][b], dp[a][b+1], dp[a][b-1])
    #             else:
    #                 tmp = min(dp[a-1][b], dp[a][b-1])
    #             dp[a][b] = l[a][b] + tmp
    # print(dp)
    # answers.append(dp[n-1][n-1])

for a in range(len(answers)):
    print("Problem " + str(a+1) + ":" + str(answers[a]))

[[3, 10, 12, 12, 13], 
 [5, 13, 12, 21, 14],
 [6, 8, 9, 17, 15], 
 [15, 16, 18, 19, 15],
 [18, 22, 23, 20, 20]]

[[3, 10, 12, 12, 13], 
 [5, 13, 9, 21, 14], 
 [6, 8, 9, 17, 15],
 [15, 16, 18, 17, 15], 
 [18, 22, 23, 18, 20]]