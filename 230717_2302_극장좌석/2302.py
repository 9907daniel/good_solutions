# 13:44 ~ 14:06
#
# vip 고정시키고 서로 바꿔가면서 count를 이어가보자
#
# 이중 for문을 사용해도 괜찮다
#
# 이친수문제에서 VIP기준으로 여러개 나눈 DP

n = int(input())

m = int(input())

l = [False]*(n)
dp = [1]*n

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
            
print(result)