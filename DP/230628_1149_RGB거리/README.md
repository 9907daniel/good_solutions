## RGB거리 실1 백준
https://www.acmicpc.net/problem/1149

### 소요시간 : 10분

### 알고리즘 사용 : DP
- 전형적인 이진 DP 문제
- 전에꺼를 고려할때 현재 + 전꺼중 안한거 2개 의 최솟값을 계속 구하면 된다


### 단계
- 생략



### 복습
```py
dp = [[0,0,0] for _ in range(n)]
dp[0] = graph[0]

for a in range(1, n):
    # 첫번째로 간다고 가정했을때, 그전 다른 색깔 두개 비교
    dp[a][0] = min(graph[a][0]+ dp[a-1][1], graph[a][0]+ dp[a-1][2])
    dp[a][1] = min(graph[a][1]+ dp[a-1][0], graph[a][1]+ dp[a-1][2])
    dp[a][2] = min(graph[a][2]+ dp[a-1][0], graph[a][2]+ dp[a-1][1])
    
print(min(dp[n-1]))
```