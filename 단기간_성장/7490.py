# 16:08 ~ 
# T = 10
# N = 최대 9
#
# DFS / 백트래킹으로 하면 될듯한데..
# 아니면 그냥 BFS로 하면은 안되나
#

from collections import deque

t = int(input())

from copy import deepcopy

def possible(l, visited):
    answers = []

    q = deque()
    q.append((0, l[0],[l[0]], []))
    
    while q:
        print(q)
        current, summed, track, calcualte = q.popleft()
        
        if current == len(l)-1:
            if summed == 0:
                answers.append(track)
    
        else:
            calcualte.append("+")
            copied = deepcopy(track)
            copied.append(l[current+1])
            q.append((current+1, summed+l[current+1], copied, calcualte))
            calcualte.pop()
            
            calcualte.append("-")
            copied = deepcopy(track)
            copied.append(l[current+1])
            q.append((current+1, summed-l[current+1], copied, calcualte))
            track.pop()
            calcualte.pop()
            
            calcualte.append(" ")
            added = str(track[-1])+str(l[current+1])
            copied = deepcopy(track)
            copied.append(int(added))
            q.append((current+1, summed-track[-1]+int(added), track, calcualte))
            calcualte.pop()
    
    return answers

for _ in range(t):
    n = int(input())
    l = [a+1 for a in range(n)]
    visited = [False]*n
    possible(l, visited)