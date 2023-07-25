#
# 09:10 ~ 09:34
#
# 입출력 : 100,000 -> On^2 까지는 가능할듯
#                -> 테케가 있기 때문에 그냥 On (?)
# 알고리즘 : DP
#
#

t = int(input())

results = []

for _ in range(t):
    n = int(input())
    
    dp = [[0]*2 for _ in range(n)]
    
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    
    if n == 1:
        results.append(max(l1[0],l2[0]))
        continue
    if n ==2:
        results.append(max(l1[0]+l2[1], l1[1]+l2[0]))
        continue
    
    # 0번 인덱스
    dp[0][0] = l1[0]
    dp[0][1] = l2[0]
    # 1번 인덱스
    dp[1][0] = l1[1]+dp[0][1]
    dp[1][1] = l2[1]+dp[0][0]
    
    for a in range(2, n):
        dp[a][1] = max(dp[a-2][0],dp[a-2][1],dp[a-1][0]) + l2[a]
        dp[a][0] = max(dp[a-2][1],dp[a-2][0],dp[a-1][1]) + l1[a]
    
    results.append(max(dp[n-1][0],dp[n-1][1]))


for a in results:
    print(a)