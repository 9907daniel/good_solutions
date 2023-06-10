# 11:52
# input이 높아서 n^2는 안된다
# 진행하며
import heapq

def solution(n, k, enemy):
    answer = 0
    health = 0
    q = []
    
    for a in enemy:
        heapq.heappush(q, -a) # to use for biggest number
        health += a
        if health > n:
            if k < 1:
                break
            k -= 1
            biggest = heapq.heappop(q)
            health -= biggest # + because biggest should be a negative
        answer += 1
            
    print(answer)
            
            
            
            