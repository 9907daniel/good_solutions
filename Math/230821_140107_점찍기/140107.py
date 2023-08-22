# 
# 09:17 ~ 09:58
#
#
# 결론 : 풀이 1) 이진탐색법
#          -> 요즘 이진탬색법을 많이 생각해서 괜히.. 
#          -> 그래도 최악의 경우에는 TLE이다
#
#          -> 수학적으로 생각을했다
#
#       풀이 2) 공식
#           -> 이게 이렇게 풀리네..
#
#    0,1,2,3,4, .. 
#
#       1) 거리는 = x^2 + y^2 이다
#       2) x는 iterate를 해주면서 이미 알게 된다
#
#       3) 즉 y^2 = (거리 - x^2)//k
#           y = ^ 곳식의 루트값
#
#
#      반례 : 어느정도 찍어서 맞춤

import math

def solution(k, d):
    
    count = 0
    for a in range(0,d,k):
        current_sum = int((d*d)-(a*a))
        rooted = int(math.sqrt(current_sum))
        count += (rooted//k)+1
        
    if d % k == 0:
        return count +1
    else:
        return count

    
    
    