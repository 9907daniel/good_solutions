# 10:23 ~ 12:05 FAIL
#
# 풀이1) 백트래킹으로 푼다
# 0. 5개 메소드를 만든다 1x1, 2x2 ...5x5
# 1. 이어져있는 '섬'을 보는것과 같이 한다. 즉, 하나의 외딴 섬 1의 조합 중 최소를 구한다
# 2. visited처리 후 진행
#
from copy import deepcopy
import sys

def two(graph, a,b, visited):
    tmp = deepcopy(visited)
    if a+1<10 and b+1<10:
        for c in range(2):
            for d in range(2):
                if graph[a+c][b+d] == 0 or visited[a+c][b+d] == True:
                    return False, tmp, tmp
                visited[a+c][b+d] = True
        return True, visited, tmp
    else:
        return False, tmp, tmp

def three(graph, a,b, visited):
    tmp = deepcopy(visited)
    if a+2<10 and b+2<10:
        for c in range(3):
            for d in range(3):
                if graph[a+c][b+d] == 0 or visited[a+c][b+d] == True:
                    return False, tmp,tmp
                visited[a+c][b+d] = True
        return True, visited, tmp
    else:
        return False, tmp, tmp

def four(graph, a,b, visited):
    tmp = deepcopy(visited)
    if a+3<10 and b+3<10:
        for c in range(4):
            for d in range(4):
                if graph[a+c][b+d] == 0 or visited[a+c][b+d] == True:
                    return False, tmp, tmp
                visited[a+c][b+d] = True
        return True, visited, tmp
    else:
        return False, tmp, tmp

def five(graph, a,b, visited):
    tmp = deepcopy(visited)
    if a+4<10 and b+4<10:
        for c in range(5):
            for d in range(5):
                if graph[a+c][b+d] == 0 or visited[a+c][b+d] == True:
                    return False, tmp, tmp
                visited[a+c][b+d] = True
        return True, visited, tmp
    else:
        return False, tmp, tmp


def max_five(graph, a,b, visited):
    length = 1
    for l in range(2, min(10 - b, 10 - a, 5) + 1):
        for i in range(b, b + l):
            for j in range(a, a + l):
                if graph[j][i] == 0 and visited[j][i]:
                    return length
        length += 1
    return length
    
def check_if_finish(graph,visited, floor):
    for a in range(floor, 10):
        for b in range(10):
            if graph[a][b] == 1 and visited[a][b] != True:
                return True, a, b
    return False,a,b

answer = 1e8
def combinations(graph, visited, count, papers, floor):
    
    global answer
    i,a,b = check_if_finish(graph, visited, floor)
    
    if i:
        check5,tmp5,visited = five(graph, a,b, visited)
        if check5 and papers[4] > 0:
            papers[4] -= 1
            combinations(graph, tmp5, count+1, papers, a)
            papers[4] += 1
            
        check4,tmp4,visited = four(graph, a,b, visited)
        if check4 and papers[3] > 0:
            papers[3] -= 1
            combinations(graph, tmp4, count+1, papers, a)
            papers[3] += 1
            check2,tmp2,visited = two(graph, a,b, visited)

        check3,tmp3,visited = three(graph, a,b, visited)
        if check3 and papers[2] > 0:
            papers[2] -= 1
            combinations(graph, tmp3, count+1, papers, a)      
            papers[2] += 1
        
        check2,tmp2,visited = two(graph, a,b, visited)
        if check2 and papers[1] > 0:
            papers[1] -= 1
            combinations(graph, tmp2, count+1, papers, a)
            papers[1] += 1
        
        if visited[a][b] != True and graph[a][b] == 1 and papers[0] > 0:
            tmp1 = deepcopy(visited)
            tmp1[a][b] = True
            papers[0] -= 1
            combinations(graph, tmp1, count+1, papers, a)
            papers[0] += 1

    else:
        answer = min(answer, count)

graph = []

for _ in range(10):
    graph.append(list(map(int, input().split())))
    
visited = [[False]*10 for _ in range(10)]

papers = [5,5,5,5,5]

combinations(graph, visited,0, papers, 0)

if answer == 1e8:
    print(-1)
else:   
    print(answer)

