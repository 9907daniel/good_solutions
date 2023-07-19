# 13"32 ~ 13"42
#
# 입력값 : 90이기 때문에 조합은 힘들다
 
n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    dp = [0]*(n)
    dp[0] = 1
    dp[1] = 1
    
    for a in range(2, n):
        dp[a] = dp[a-1]+dp[a-2]
    print(dp[n-1])