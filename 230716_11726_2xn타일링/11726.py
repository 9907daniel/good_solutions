n = int(input())

if n == 1:
    print(1)
elif n ==2:
    print(2)
else:
    dp = [0]*n
    dp[0] = 1
    dp[1] = 2
    for a in range(2,n):
        dp[a] = dp[a-2]+dp[a-1]
        
    print(dp[n-1]%10007)