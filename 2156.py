#
# 09:05 ~ 09:36 + 10:06 ~ 10:37 (Fail)
#
# 연속된 3잔을 마시지 않으면서 최대를 마신다
# -> 현재 시점에서 최대를 계속해서 고려
#    -> 하지만 전꺼와 전전꺼를 마셨다면 현재는 마실 수 없다
#       --> 현재 시점에서 예전꺼를 추가하는게 맞다 (?) (현재에서 전꺼의 Max를 비교)
#
# 현재 시점에서 앞에꺼를 마시느냐 뒤에꺼를 마시느냐..? 
#
#       6 10 13 9 8 1 7 4 5 6 20 30 2 4 4 4 2 1
#
#               9 위치에서 이때까지 최대를 어떻게 고려할까
#          i) 뒤에세 3,2개를 먹는다 + 다음꺼를 먹는다 -> current+1에 최대치로 기록
#          ii) 뒤에서 1을 먹는다 + 다다음꺼부터 먹는다 -> current+2에 최대치로 기록
#
#          i) 현재 시점에서 -2를 먹고 +1에 기록
#          i) 현재 시점에서 -1을 먹고 +2에 기록
#


# [0] 은 전꺼의 DP까지 담고
# [1] 은 전전꺼의 DP까지 담아서 각자 비쇼를 한다

# dp = [[0]*2 for _ in range(n+1)]

# 앞에 두개짜리한테 : 그냥 나의 DP를 선택할래? 아니면 앞에 있는 DP를 선택할래

#  6 10 13 9 8 1

# dp[0][0] = 0        # 0
# dp[0][1] = l[0]     # 6

# for a in range(1, n):
#     # 6 + _ -> 6+13        -> 
#     dp[a][0] = dp[a-1][1]
#     # _ + 10 -> 10+13      -> 
#     dp[a][1] = dp[a-1][0] + l[a]

# print(dp)

# [[0, 6], [6, 10], [10, 19], [19, 19], [19, 27], [27, 20], [0, 0]]

###############################
###############################
###############################

n = int(input())
l = []

dp = [0]*10001

for _ in range(n):
    l.append(int(input()))

dp[0] = l[0]
dp[1] = dp[0] + dp[1]

# 여기서 부터 상황을 고려해 보자 : 
# i) 현재 먹고 현재-2먹는다 
# ii) 현재 먹고 전꺼 먹고 전전꺼 먹지 않는다 -> 전전전꺼를 추가해햐한다
# iii) 현재꺼 먹지 않고, 전꺼를 그대로 가져온다
dp[2] = max(l[2]+dp[0], l[2]+dp[1]-l[0], dp[1])

for a in range(3, n):
    dp[a] = max(l[a]+dp[a-2],l[a]+l[a-1]+dp[a-3] )










###############################
###############################
###############################
# dp = [0]*(n+1)
# dp[0] = l[0]
# dp[1] = l[1]+dp[0]
# # 현재 시점에서 전꺼를 뺸거 vs 현재꺼를 비교해서 넣자
# for a in range(2,n):
#     dp[a] = max(dp[a-1]+l[a]-l[a-2]+l[a-2], dp[a-2]+l[a])
    
# print(dp)