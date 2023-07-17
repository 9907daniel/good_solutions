## 극장좌석 실1 백준
https://www.acmicpc.net/problem/2302

### 소요시간 : 20분

### 알고리즘 사용 : DP
- 이친수 문제 (n-1)+(n-2)를 여러개로 나눈 문제이다
- 반례값을 조금은 생각해야한다 (VIP Edgecase)

### 단계
- 생략


### 복습
```
 for _ in range(m):
    x = int(input())
    l[x-1] = True
    

result = 1
for a in range(1,len(l)):
    
    # VIP
    if l[a] == True and a == 0:
        dp[a] = 1
    # VIP 이고 1번째 아니다
    elif l[a] == True and a != 0:
        # 옆에도 VIP가 아니면
        if l[a-1] != True:
            result = result*dp[a-1]
    # 일반석이다면
    else:
        # 전자리가 VIP라면
        if l[a-1] == True:
            dp[a] = 1
        else:
            # 전자리가 VIP가 이닌데, 1,2번이라면
            if a == 0:
                dp[a] = 1
            elif a == 1:
                dp[a] = 2
            else:
                dp[a] = dp[a-2]+dp[a-1]
        if a == len(l)-1:
            result = result*dp[a]

```
