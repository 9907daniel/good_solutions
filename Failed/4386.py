# 13:08 ~ 13:27 ~ 53
# 
# 최소값을 구하는 문제이기 떄문에 다익스토 / 플로이드 와샬이다
# BFS로 풀어도 괜찮은듯..? 
#
# 1,1 -> 2,2 -> 2
# 2,2 -> 2,4 -> 2
#
#
# 1) 완탐으로 한다면 -> 100 펙토리얼
# 2) 그리디 할떄 최적의 경우를 보장하나?
#
# 모든 경우에서 모든 경위의 최적을 구하는 플로이드 와샬이 / MST
import math

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b :
        parent[b] = a
    else:
        parent[a] = b
    
    
n = int(input())
parent = []

for a in range(n+1):
    parent.append(a)

l = []

for _ in range(n):
    l.append(list(map(float, input().split())))
             
distance = []

for a in range(n-1):
    for b in range(a+1, n):
        root_square = math.sqrt((l[a][0]-l[b][0])*(l[a][0]-l[b][0])+(l[a][1]-l[b][1])*(l[a][1]-l[b][1]))
        distance.append((root_square, a, b))

distance.sort()
answer = 0
for a in range(len(distance)):
    current_distance,x,y = distance[a]

    if find(x) != find(y):
        union(x,y)
        answer += current_distance
    
answer = answer*100
answer = int(answer)
answer = answer / 100
print(answer)