# 10:10 ~ 10:45
#
# 20 -> 
# 1,2,1,2,1   10 1 2
# 1,2,1,2,1,10 1 2
# ...
# 10.    1,2,1,2,1,2,1
#
# 더 작은거에다가 pop을 하고 추가를 해주는 완탐.? 
#
# 반례) 
# 1) 처음부터 똑같을때
# 2) 길이가 1인데 서로 다를때
# 3) 처음부터 합이 홀수 일떄
#
#
# 처음에 sum() 활용해서 TLE


from collections import deque

def solution(queue1, queue2):
    total_sum = sum(queue1) +sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_1 = sum(q1)
    sum_2 = sum(q2)
    count = 0
    
    if total_sum % 2 == 1:
        return -1
    
    if len(q1) == 1 and sum(q1) != sum(q2):
        return -1
    if sum(q1) == sum(q2):
        return 0
    
    while True:
        # 반례 -> len(total)가 아니라 len(total)*2 -> 양방향의 모든 경우의 수
        if count > (len(q1)+len(q2)):
            return -1
        
        if sum_2 > sum_1:
            x = q2.popleft()
            q1.append(x)
            sum_1 += x
            sum_2 -= x
        else:
            x = q1.popleft()
            q2.append(x)
            sum_2 += x
            sum_1 -= x

        count += 1
        if sum_1 == sum_2:
            return count
    
    
    
    
    
    
    
    