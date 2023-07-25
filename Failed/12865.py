#
#
# 09:36 ~ 09:45 + 10:37
#
# 어제 문제와 비슷 -> 합을 수한뒤에 범위를 벗어난지 확인한다
#
# 입력이 100이어서 조합은 힘들다

from itertools import combinations

n,k = map(int, input().split())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

# for b in range(n):
#     for a in combinations(l, b+1):
        