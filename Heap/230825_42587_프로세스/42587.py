# 19:07 ~ 
#
# 1) 힙이랑 큐를 동시에 관리하며 순서를 비교하는거는 어떨까..? 
#
#   2 1 3 2
#   3 2 2 1
#
#  if current == same 값 -> pop
#

from collections import deque
from heapq import heappop, heappush

def solution(priorities, location):
    
    q = []
    priorities = deque(priorities)
    
    # -3 -2 -2 -1
    for a in priorities:
        heappush(q, -a)
    
    
    count = 1
    while True:
        current = priorities.popleft()
        comparison = -(q[0])
        
        if location == 0:
            if current == comparison:
                return count
            else:
                priorities.append(current)
                location = len(priorities)-1
        else:
            if current == comparison:
                heappop(q)
                count += 1
            else:
                priorities.append(current)
            location -= 1
            
            
  