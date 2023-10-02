
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


gg = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]

[[1, 6, 11, 16, 21], 
 [2, 7, 12, 17, 22], 
 [3, 8, 13, 18, 23], 
 [4, 9, 14, 19, 24],
 [5, 10, 15, 20, 25]]


def rotate(l, angle=90):
    arr = list(map(list, zip(*gg[::-1])))
    return arr

print(rotate(gg))

def rotate_anti(l, angle=90):
    arr = list(map(list, zip(*gg)))[::-1]
    return arr

print(rotate_anti(gg))

def transform(matrix):
    arr = list(map(list, zip(*matrix)))
    return arr

print(transform(gg))


# from collections import deque

# alphabet = deque(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])


# print(alphabet.pop(alphabet.index('B')))


# N, K = map(int, input().split())
# # 3 -2 -4 -9 0 3 7 13 8 -3
# temperatures = list(map(int, input().split()))
# if K == 1:
#     print(max(temperatures))
#     exit()

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


# p1, p2 = 0, K
# temp = sum(temperatures[p1:p2])
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