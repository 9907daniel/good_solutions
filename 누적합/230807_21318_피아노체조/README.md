
## 피아노체조 실1 bj
https://www.acmicpc.net/problem/21318

### 알고리즘 사용 : 누적합 (DP)
- 완탐 그리디는 시간초과가 난다 (테스트 케이스가 100만이다)
- 한번 iterate를 하고 결과들을 기록한다

### 단계
- 한번에 기록

### 코드리뷰
```py
n = int(input())
l = list(map(int, input().split()))

q = int(input())
g = []

for _ in range(q):
    g.append(list(map(int, input().split())))
    
    
if n == 1:
    for _ in range(q):
        print(0)
else:
    dp = [0]*n
    if l[0] > l[1]:
        dp[0] = 1
    else:
        dp[0] = 0

    for a in range(1,len(l)):
        if l[a] < l[a-1]:
            dp[a] = dp[a-1]+1
        else:
            dp[a] = dp[a-1]
                
    results = []
    for a in g:
        if a[0] == a[1]:
            count = 0
        else:
            count = dp[a[1]-1] - dp[a[0]-1]
        results.append(count)

    for a in results:
        print(a)
      
```
