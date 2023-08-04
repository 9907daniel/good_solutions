# 13:50 ~ 2:30
#
# 문제 : M을 마추는 최소 도수 합
# 1) 정렬
# 2) 그리디..?
#
# 예전 무적권 문제랑 비슷한듯한데..
#  
# 4 3 = 1.333  
# 4 6 = 0.666
# 3 3 = 1
# 2 5 = 0.4
# 1 4 = 0.25
#
#
# N개는 꼭 선택을 하야하는데.. 어떻게 최소값을 마추지..?
#
# 탐색을 전부 하는제, 무조건 추가를 하다, 만약 == N이 되고서 부터는 끝까지 비교를 하면서 추가해보다
#
#

import heapq
import sys

# 축제기간, 맞춰야할 최소 선호도, 맥주 종류 
n,m,k = map(int, input().split())

l = []
for _ in range(k):
    l.append(list(map(int, input().split())))
    
# l.sort(key=lambda x:(x[0]/x[1]), reverse = True)
l.sort(key=lambda x:(x[1],x[0]))


q = []
total = 0
for a in range(len(l)):
    if len(q) == n:
        x = heapq.heappop()

        if total >= m:
            answer = 
            
        else:
            total -= heapq.heappop(q)
        
    else:
        heapq.heappush(q, l[a])
        total += l[a]
    




# total = 0
# liver = 0

# start = 0
# while total < m:
#     total += l[start][0]
#     liver += l[start][1]
#     start += 1

# print(liver)
    
    
    