# 19:27 ~ 20:20
# 
# 총 있는 장의 숫자 = 100만
# 
# 풀이 : 
# 합의 평균이 가장 가깝게 만들어서..? 
# 합한 바용이 최소가 괴든것이 뭘까..? 
# 
# 최소 비용) 매 순간에 최소를 더하는 방법이다 
# -> 그렇다면 항상 정렬을 유지해야하는데.. 그러는 방법이.>? 
# 힙을 사용하자!
#
#

from heapq import heappush, heappop

t = int(input())

answers = []

for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    
    q = []

    for a in range(len(l)):
        heappush(q, l[a])
        
    summed = 0
    
    
    while q:
        if len(q) > 1:
            x1 = heappop(q)
            x2 = heappop(q)
            heappush(q, x1+x2)
            summed += (x1+x2)
        else:
            x1 = heappop(q)
            summed += x1
            break
        
    answers.append(summed-sum(l))

for a in answers:
    print(a)
    



