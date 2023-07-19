# 12 : 08
#
#
# 반례 : 수열 크기가 1일때
#
#
n = int(input())

l = list(map(int, input().split()))

dp = [0]*n

dp[0] = l[0]

for a in range(1, len(l)):
    dp[a] = l[a]
    for b in range(a-1,-1,-1):
        if l[b] < l[a]:
            dp[a] = max(dp[a], l[a]+dp[b])
        
print(dp)
print(max(dp))