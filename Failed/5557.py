#
# 14:08
#
# 입출력 : 100 이기 떄문에 모든 조합을 구한다면 무리가 될듯 하다 100!
#
# 이차배열 DP를 통해 트리 형식으로 내려가면 어떨까?
#
#
# 8 3 2 4 8 7 4 0 8 8 
# 
# 8 -> 8+3  ->  8+3+2
#               8+3-2
#      8-3  ->  8-3+2
#               8-3-3 ...
# -> 2^100 ...
#
# 차라리 현재 가능한것 중에 최대값/ 최소값을 기록하며,.?
#
#  8 11 13 17 25 32 32 40 48
#             11
#
#
#
#  8 5 3 -1 -9 -16 -16 -24 -32
#
#
# 배열을 세로 DP로 풀어보자!!@!@!@
# 
# 힌트는 바로 가로 n = 100, 세로 n = 20

n = int(input())
l = list(map(int, input().split()))

dp = [[0]*n for _ in range(21)]

dp[l[0]][0] = 1

for a in range(1, n-1):
    for b in range(21):
        if dp[b][a-1]:
            if 0 <= b-l[a]:
                dp[b-l[a]][a] += dp[b][a-1]
            if b+l[a] <= 20:
                dp[b+l[a]][a] += dp[b][a-1]

print(dp)

# 8    3        2              4                     8                              7 2 4 0 8 8
# 8 -> 5, 11 -> 3, 7, 9, 13 -> 7 3 11 5 13 9 17 ->  15 11 19 3 13 5 
[[0, 0, 0, 0,   0, 0, 1, 2, 4, 8, 10], 
 [0, 0, 0, 0,   1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 1, 3, 6, 12, 12],
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 2, 4, 8, 8, 10],
 [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 3, 5, 10, 12, 10],
 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
 [1, 0, 0, 0, 0, 2, 3, 4, 8, 10, 16], 
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 2, 4, 6, 12, 12, 24],
 [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 2, 2, 4, 8, 10, 16], 
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 3, 6, 12, 10, 12],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 1, 3, 6, 8, 10], 
 [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 2, 3, 6, 12, 12], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 1, 1, 2, 8, 10]]



[[0, 0, 0, 0, 0, 0, 1, 1, 2, 1, 1], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1],
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1], 
 [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 2, 2, 2, 1, 1], 
 [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0], 
 [1, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2],
 [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 2],
 [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 2, 2, 2, 1, 1],
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 1, 1, 2, 2, 1, 1],
 [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 2, 1, 2, 1, 1], 
 [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0], 
 [0, 0, 0, 0, 0, 1, 1, 1, 2, 1, 1]]