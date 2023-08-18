#
# 0806 ~ 0846
# 입출력 : K : 100,000 & N : 100,000
#
# 알고리즘 : DP 중에서도 전형적인 KNAP SAP 문제이다
# -> 냅샙은 세로 DP 라고 생각하면 될까?
#
# 무게   가치
# 4     7
# 6     13
# 4     8 
# ...   ... 
#
# 탐색을 하면서 
# l = 2,13   4,8   3,6 ...
# 0 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 13 13 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 
# 0 8 0 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
# 0 21 0 0 0 0 0 
# 0 0 0 0 0 0 0 0 
#

n, k = map(int, input().split())

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

    print(max(dp[-1]))





