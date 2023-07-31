
# dic = {}
# dic[3] = 3
# dic[1] = 1
# dic[2] = 3

# print(dic.values())

# print(dic)
# x = sorted(dic)
# # print(x)


# # two pointer
# # 연속적인 날짜를 가리키면서 이동

# 10 2
N, K = map(int, input().split())
# 3 -2 -4 -9 0 3 7 13 8 -3
temperatures = list(map(int, input().split()))
if K == 1:
    print(max(temperatures))
    exit()

# p1, p2 = 0, 1
# temp = temperatures[p1] + temperatures[p2]
# maxV = 0
# while True:
#     if p2 - p1 + 1 == K:
#         maxV = max(maxV, temp)
#         temp -= temperatures[p1]
#         p1 += 1
#     if p2 + 1 < len(temperatures):
#         p2 += 1
#         temp += temperatures[p2]
#     else:
#         break
# print(maxV)


p1, p2 = 0, K
temp = sum(temperatures[p1:p2])
maxV = 0
while True:
    if p2 - p1 + 1 == K:
        maxV = max(maxV, temp)
        temp -= temperatures[p1]
        p1 += 1

    if p2 + 1 < len(temperatures):
        p2 += 1
        temp += temperatures[p2]
    else:
        break