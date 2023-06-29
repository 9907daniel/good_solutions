n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
dp = [[0,0,0] for _ in range(n)]
dp[0] = graph[0]

for a in range(1, n):
    # 첫번째로 간다고 가정했을때, 그전 다른 색깔 두개 비교
    dp[a][0] = min(graph[a][0]+ dp[a-1][1], graph[a][0]+ dp[a-1][2])
    dp[a][1] = min(graph[a][1]+ dp[a-1][0], graph[a][1]+ dp[a-1][2])
    dp[a][2] = min(graph[a][2]+ dp[a-1][0], graph[a][2]+ dp[a-1][1])
    
print(min(dp[n-1]))