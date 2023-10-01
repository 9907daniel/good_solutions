# 12:02 ~ 12:40
# 

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

# 0->row, 1->column, 2-> diagaonal
dp = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]


dp[0][1][0] += 1
# print(dp[0])


for a in range(n):
    for b in range(n):
        if len(dp[a][b]) != 0 and graph[a][b] != 1:
            for c in range(3):
                if c == 0:
                    if b+1 < n and graph[a][b+1] != 1:
                        dp[a][b+1][c] += dp[a][b][0]
                        dp[a][b+1][c] += dp[a][b][2]
                if c == 1:
                    if a+1 < n and graph[a+1][b] != 1:
                        dp[a+1][b][c] += dp[a][b][1]
                        dp[a+1][b][c] += dp[a][b][2]
                if c == 2:
                    if b+1 < n and a+1 < n and graph[a+1][b+1] != 1 and graph[a+1][b] != 1 and graph[a][b+1] != 1:
                        dp[a+1][b+1][c] += dp[a][b][0]
                        dp[a+1][b+1][c] += dp[a][b][1]
                        dp[a+1][b+1][c] += dp[a][b][2]

print(sum(dp[n-1][n-1]))
# print(dp)

# [[[0, 0, 0], [1, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
#  [[0, 0, 0], [0, 0, 0], [0, 0, 1], [1, 0, 0], [1, 0, 0]], 
#  [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1]],
#  [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 1, 1], [1, 1, 1]], 
#  [[0, 0, 0], [0, 0, 0], [0, 1, 0], [0, 2, 1], [1, 2, 2]]]