# 15:47 ~ 
#
# 두가지 경우가 있다
# 1) 물건을 넣지 않는다
# 2) 물건을 넣는다
#
# 최대 K만큼을 넣을 수 있기 때문에 KNAPSACK 문제이다
#
# 메모리는 어디까지 TLE인가..? 
n,k = map(int, input().split())

l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

dp = [[0]*(k+1) for _ in range(n)]

if n == 1:
    if l[0][0] <= k:
        print(l[0][1])
    else:
        print(0)
else:
    dp[0][l[0][0]] = l[0][1]
    
    for a in range(1, len(l)):
        for b in range(len(dp[a])):
            if dp[a-1][b] != 0:
                # 이번꺼를 추가하지 않고 전껏들을 전부 가져오기
                dp[a][b] = max(dp[a][b], dp[a-1][b])
                
                # 저번가방에 + 현재꺼 추가하기
                if b+l[a][0] <= k:
                    dp[a][b+l[a][0]] = max(dp[a][b+l[a][0]], dp[a-1][b]+l[a][1])
                
                # 저번꺼 말고 이번꺼만 추가히기
                if l[a][0] <= k:
                    dp[a][l[a][0]] = max(dp[a][l[a][0]], l[a][1])
    # 
    # 10,000,000
    # 1억 = 300mb
    #  0  0 0 0 0 0 0 0 0 0 0
    #  0 -0
    #  0  0
    #  0  7 
    #  0  0
    #  0    13
    #  0    20
    #
    #    15
       
    
            
            
            
    # for a in range(1, len(l)):
    #     for b in range(len(dp[a])):
    #         if dp[a][b] != 0:
    #             dp[a][b] = max(dp[a][b], dp[a-1][b])
                
    #             if b+l[a][0] <= k:
    #                 dp[a][b+l[a][0]]