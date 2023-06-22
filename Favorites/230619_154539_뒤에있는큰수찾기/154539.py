# 10:23 ~
# 입력 : 1,000,000 -> 그리디이고 O(n)으로 해결해야 할꺼 같다
# 큐 / 스택을 사용해도 됀찮을꺼 같다

from collections import deque

def solution(numbers):
    q = []
    results = [-1]*(len(numbers))
    
    # 0 ~ numbers-2 까지(?)
    for a in range(len(numbers)):
        # 만약 스택이 비어 있다면 일단 추가한다
        if len(q) == 0:
            q.append([numbers[a],a])
        
        # 비어있지 않다면 비교를 한다
        else:
            b = len(q)-1
            while b != -1:
                if numbers[a] > q[b][0]:
                    results[q[b][1]] = numbers[a]
                    q.pop()
                    b -= 1
                else:
                    break
            q.append([numbers[a],a])
    
    return results
                
                
                
                
                