## 점프 실1 백준
https://www.acmicpc.net/problem/1890

### 소요시간 : 1시간

### 알고리즘 사용 : DP
- 생각하기는 굉장히 간단한 DP문제이지만 마지막 종료 조건이 조금 위외였다
    - n-1,n-1일때 추가를 하지 않는다
    - 실전이었으면 시간이 부족했을꺼 같다
- 최대값 : 거리값 더해주기
- 모든 경우 : 값을 더하지 말고 +1 / +dp의 느낌으로

### 단계
- 이차원 DP 생성
- 건너뛰기 기록
- n-1 n-1 일때 종료



### 복습
```py
dp = [[0]*n for _ in range(n)]
dp[0][0] = 1


for a in range(n):
    for b in range(n):
        if a ==(n-1) and b == (n-1):
            break

        if b+graph[a][b] < n and dp[a][b] != 0:
            dp[a][b+graph[a][b]] += dp[a][b]
        
        if a+graph[a][b] < n and dp[a][b] != 0:
            dp[a+graph[a][b]][b] += dp[a][b] 
```