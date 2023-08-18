## 평범한 배낭 골5 백준
https://www.acmicpc.net/problem/12865

### 소요시간 : 40분

### 알고리즘 사용 : DP + KnapSack
- Knap Sack의 기본기가 되는 DP 문제이다
- Column을 생각하기 보다는 Row를 생각하자
    - Row에서 전 Column을 보고 0 이 아닌값들에서 모든 겨우의 수를 생각하면 된다
- 즉 : KnapSack은 '물건을 넣는 방법으로 가능한 모든 경우'를 시도해보기 보단, '물건을 넣었을때 가능한 모든 결과값'에 대한 최적해를 구하는 문제이다
- 같은 경우에 겹치는 경우가 있으니 모든것을 새로 가져올떄 Max()로 비교를 해주자

### 단계
- 생략


### 복습
```py
dp[0][l[0][0]] = l[0][1]

for a in range(1, len(l)):
    for b in range(len(dp[a])):
        if dp[a-1][b] != 0:
            # 이번꺼를 추가하지 않고 전껏들을 전부 가져오기
            dp[a][b] = max(dp[a][b], dp[a-1][b])
            
            # 저번가방에 + 현재꺼 추가하기
            if b+l[a][0] <= k:
                dp[a][b+l[a][0]] = max(dp[a][b+l[a][0]], dp[a-1][b]+l[a][1])
            
            # 저번꺼 말고 이번꺼만 추가히기
            if l[a][0] <= k:
                dp[a][l[a][0]] = max(dp[a][l[a][0]], l[a][1])
```