#  13:55 ~ 
#
#
# 풀이가 매게변수 탐색 문제 같다..
# 
# 1 6 
# 8 12
# 13 17
# 
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
#   _ _ _ _ _ _
#                 _ _ _ _ _ _ 
#                              _ _  _   _  _ 
# 
#   _ _ _ _ _ _   _ _ _ _ _ _  _ _ _ _ _ 
#
#
# 이 문제는 그냥 무조건 .. 그리디
import math

n,l = map(int, input().split())

puddles = []

for _ in range(n):
    x,y = list(map(int, input().split()))
    puddles.append([x,y])
    
puddles.sort(key=lambda x :(x[0],x[1]))

count = 0
current_last_wood = puddles[0][0]

for a in range(len(puddles)):
    # 현재 지점에서 전 나무판이 시작점 이상으로 닿는다면..
    if current_last_wood <= puddles[a][1]:
        if current_last_wood < puddles[a][0]:
            current_last_wood = puddles[a][0]
        length = puddles[a][1]-current_last_wood
        r = 1
        if length % l == 0:
            r = 0
        tmp = length//l + r
        current_last_wood += tmp*l
        count += tmp
         
print(count)
