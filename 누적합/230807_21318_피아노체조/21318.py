# 10:08 ~ 10:41
#
# 입출력 : 100만*100만 => 1억.. -> 시간 제한은 0.5초...
#        n 도 TLE 날수도 있다
#
# 풀이 1) : 그리디적으로 풀 수 있을듯 하다..?
#          = TLE
#
#
# 풀이 2) DP적으로..? 기록을 해볼까..?
#          = 누적합 연습..
#
# 풀이 3) 이진탐색으로 풀어야 할수도..
#

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










    # n = int(input())
    # l = list(map(int, input().split()))

    # q = int(input())
    # g = []

    # for _ in range(q):
    #     g.append(list(map(int, input().split())))
        
    # results = []
    # for a in g:
    #     current = l[a[0]-1:a[1]]

    #     count = 0
        
    #     for a in range(len(current)-1):
    #         if current[a] > current[a+1]:
    #             count += 1
        
    #     results.append(count)
        
    # for a in results:
#     print(a)