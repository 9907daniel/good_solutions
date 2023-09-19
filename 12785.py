# 13:53 ~ 
# 
# 둘다 나누면 된다..? 
# 
# 
# 

w, h = map(int, input().split())
toast_x, toast_y = map(int, input().split())

graph = [[0]*(w) for _ in range(h)]
dp = [[0]*(w) for _ in range(h)]

dp[0][0] = 1

for a in range(toast_y):
    for b in range(toast_x):
        if a > 0:
            dp[a][b] += dp[a-1][b]
        if b > 0:
            dp[a][b] += dp[a][b-1]

for a in range(toast_y-1, h):
    for b in range(toast_x-1, w):
        if a > toast_y-1:
            dp[a][b] += dp[a-1][b]
        if b > toast_x-1:
            dp[a][b] += dp[a][b-1]

print(dp[h-1][w-1]%1000007)




