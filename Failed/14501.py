n = int(input())

days = []

for a in range(n):
    days.append(list(map(int, input().split())))

dp = [0]*(n)

dp[0] = days[0][1]

for a in range(1,len(days)):
    # if a == len(days)-1 and days[a][0] == 1:
    #     dp[a] += days[a][1]
    
    if a+days[a][0]-1 < n:
        dp[a+days[a][0]-1] = max(dp[a+days[a][0]-1], dp[a]+days[a][1])
        
print(dp)