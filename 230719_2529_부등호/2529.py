#
# 10:37 ~ 10:55
#
# 입력값이 굉장히 낮다..
#
from itertools import permutations

n = int(input())
l = list(input().split())
nums = [a for a in range(10)]

possible = []
for a in permutations(nums, n+1):
    for b in range(len(l)):
        if l[b] == '>' and a[b] < a[b+1]:
            break
        elif l[b] == '<' and a[b] > a[b+1]:
            break
        if b == len(l)-1:
            possible.append(list(a))


possible.sort()
mini = ""
maxi = ""
for a in range(n+1):
    mini += str(possible[0][a])
    maxi += str(possible[-1][a])
print(maxi)
print(mini)


# current_max = 0
# current_min = 1e8
# for a in range(len(possible)):
#     current_min[] = min