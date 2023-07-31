# 09:04 ~ 09:25
#
# 입출력 : 100만 -> 하나의 iteration
#
# 알고리즘 : 그리디, DP, 이진탐색 ...
# 자료구조 : 힙, 
#
# 풀이법 : 언제 무적권 K을 사용할지 정하는것이 중요하다.
#
# i) 힙에다가 숫자들을 순차적으로 넣어준다
# ii) iterate 하면서 빼준다
# iii) 0이하가 되는순간 무적권을 전에 사용한척, 지나온 값들 중에서 최댓값을 더해준다
#
from heapq import heappush, heappop

def solution(n, k, enemy):
    h = []
    count = 0
    for a in range(len(enemy)):
        heappush(h, -enemy[a])
        
        # 반례 > 0 일때..? --> 왜..?
        if n-enemy[a] >= 0:
            n -= enemy[a]
        elif k > 0 and n-enemy[a] <= 0:
            x = -heappop(h)
            n += x
            n -= enemy[a]
            k -= 1
        else:
            break
        count += 1
    return count
    
            
            
            
            