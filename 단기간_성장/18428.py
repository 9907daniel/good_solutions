# 13:46 ~ 14:14
#
# N = 6 -> 6x6 -> 36개의 경우다
#
# 36*36*36 -> 완탐으로 해도 괜찮을듯하다
#
#

from itertools import combinations
from copy import deepcopy
import sys

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(str, input().split())))

teachers = []
students = []
possible = []

for a in range(n):
    for b in range(n):
        if graph[a][b] == 'S':
            students.append([a,b])
        elif graph[a][b] == 'T':
            teachers.append([a,b])
        else:
            possible.append([a,b])

def dfs(graph, teachers):
    viewable = False
    
    for a in range(4):
        # print(graph)
        if a == 0:
            teachers_x = teachers[0]
            teachers_y = teachers[1]
            
            while 0<= teachers_x:
                if graph[teachers_x][teachers_y] == 'O':
                    break
                if graph[teachers_x][teachers_y] == 'S':
                    return False
                teachers_x -= 1
        if a == 1:
            teachers_x = teachers[0]
            teachers_y = teachers[1]

            while 0<= teachers_y:
                if graph[teachers_x][teachers_y] == 'O':
                    break
                if graph[teachers_x][teachers_y] == 'S':
                    return False
                teachers_y -= 1
        if a == 2:
            teachers_x = teachers[0]
            teachers_y = teachers[1]

            while teachers_x < len(graph):
                if graph[teachers_x][teachers_y] == 'O':
                    break
                if graph[teachers_x][teachers_y] == 'S':
                    return False
                teachers_x += 1
        if a == 3:
            teachers_x = teachers[0]
            teachers_y = teachers[1]

            while teachers_y < len(graph): 
                if graph[teachers_x][teachers_y] == 'O':
                    break
                if graph[teachers_x][teachers_y] == 'S':
                    return False
                teachers_y += 1      
    return True          
        
for a in combinations(possible, 3):
    tmp = deepcopy(graph)
    for b in range(3):
        tmp[a[b][0]][a[b][1]] = 'O'
    
    count = 0
    for a in teachers:
        # print(count)
        x = dfs(tmp, a)
        if x == True:
            count += 1
        else:
            break
    # print(count)
    # print(len(teachers))
    if count == len(teachers):
        print('YES')
        sys.exit()
print('NO')
                    
