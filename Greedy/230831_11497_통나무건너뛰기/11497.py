#  
# 2 9 7 4 5
# 2 4 5 7 9
# 
# -> 2  _ _ _ 4
# -> 2 5 _ _ 4
# -> 2 5 _ 7 4
# -> 2 5 9 7 4
#

from collections import deque

t = int(input())

answer = []
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    l.sort()
    l = deque(l)

    start = 0
    end = len(l)-1
    q = [0]*len(l)
    
    for a in range(len(l)):
        x = l.popleft()

        if a % 2 == 0:
            q[start] = x
            start += 1
        else:
            q[end] = x
            end -= 1
    
    current = abs(q[0]-q[1])
    for a in range(1,len(q)-1):
        current = max(current, abs(q[a]-q[a+1]))
    answer.append(current)

for a in answer:
    print(a)
    
    
    

