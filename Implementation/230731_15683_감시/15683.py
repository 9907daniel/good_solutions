# 09:26
#
#
#
#
# 무조건 최솟값을 못 선택하는 이유 : 나중에 겹치는 부분으로 이미 커버 가능할수도..
# -> 무조건 모든 조합을 구해봐야한다
# 
# -> 한칸 씩 iterate를 하면서 그냥 모든 가능성을 전부 다 배열에 담아 확인해보자..

from copy import deepcopy

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
# [3,[0000,1101,0000]] -> 이런식으로 저장하자.. -> 나중에 그냥 sort
next = [[n*m,graph]]
numbers = [1,2,3,4,5,6]
current_min = m*n


def south(graph,a,b):
    if 0<= a-1 and graph[a-1][b] != 6:
        graph = south(graph, a-1, b)
        if graph[a-1][b] not in numbers:
            graph[a-1][b] = "#"
    return graph

def north(graph,a,b):
    if a+1<n and graph[a+1][b] != 6:
        graph = north(graph, a+1, b)
        if graph[a+1][b] not in numbers:
            graph[a+1][b] = "#"
    return graph

def east(graph,a,b):
    if b+1<m and graph[a][b+1] != 6:
        graph = east(graph, a, b+1)
        if graph[a][b+1] not in numbers:
            graph[a][b+1] = "#"
    return graph

def west(graph,a,b):
    if 0<= b-1 and graph[a][b-1] != 6:
        graph = west(graph, a, b-1)
        if graph[a][b-1] not in numbers:
            graph[a][b-1] = "#"
    return graph


def camera_one(graph, a, b, next):
    global current_min
    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)
    tmp2 = deepcopy(graph)
    tmp3 = deepcopy(graph)
    
    # 남
    x = south(tmp,a,b)
    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)
    
    # 북
    x = north(tmp1,a,b)
    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

    
    # 동
    x = east(tmp2,a,b)
    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

    
    # 서
    x = west(tmp3,a,b)
    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)


    return next

def camera_two(graph, a, b, next):
    global current_min

    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)

    # 남북
    x = south(tmp,a,b)
    x = north(tmp,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

        
    # 북
    y = east(tmp1,a,b)
    y = west(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])
    current_min = min(count, current_min)

    return next

def camera_three(graph, a, b, next):
    global current_min

    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)
    tmp2 = deepcopy(graph)
    tmp3 = deepcopy(graph)

    # 북동
    x = north(tmp,a,b)
    x = east(x,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

        
    # 동남
    y = east(tmp1,a,b)
    y = south(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])   
    current_min = min(count, current_min)
 
    
    # 남서
    y = south(tmp2,a,b)
    y = west(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])  
    current_min = min(count, current_min)

    
    # 서북
    y = west(tmp3,a,b)
    y = north(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])  
    current_min = min(count, current_min)

    return next

def camera_four(graph, a, b,next):
    global current_min

    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)
    tmp2 = deepcopy(graph)
    tmp3 = deepcopy(graph)

    # 북동서
    x = north(tmp,a,b)
    x = east(x,a,b)
    x = west(x,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

        
    # 동남북
    y = east(tmp1,a,b)
    y = south(y,a,b)
    y = north(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y]) 
    current_min = min(count, current_min)
   
    
    # 남서동
    y = south(tmp2,a,b)
    y = west(y,a,b)
    y = east(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])  
    current_min = min(count, current_min)

    
    # 서북남
    y = west(tmp3,a,b)
    y = north(y,a,b)
    y = south(y,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if y[d][e] == 0:
                count += 1
    next.append([count, y])
    current_min = min(count, current_min)

    return next
    
def camera_five(graph, a, b,next):
    global current_min

    tmp = deepcopy(graph)

    # 북동서남
    x = north(tmp,a,b)
    x = east(x,a,b)
    x = west(x,a,b)
    x = south(x,a,b)

    count = 0
    for d in range(n):
        for e in range(m):
            if x[d][e] == 0:
                count += 1
    next.append([count, x])
    current_min = min(count, current_min)

    return next
        
for a in range(n):
    for b in range(m):
        l = deepcopy(next)
        if graph[a][b] == 1:
            next = []
            for c in range(len(l)):
                next = camera_one(l[c][1],a,b,next)
        elif graph[a][b] == 2:
            next = []
            for c in range(len(l)):
                next = camera_two(l[c][1],a,b,next)

        elif graph[a][b] == 3:
            next = []
            for c in range(len(l)):
                next = camera_three(l[c][1],a,b,next)

        elif graph[a][b] == 4:
            next = []
            for c in range(len(l)):
                next = camera_four(l[c][1],a,b,next)

        elif graph[a][b] == 5:
            next = []
            for c in range(len(l)):
                next = camera_five(l[c][1],a,b,next)

print(current_min)
# next.sort(key=lambda x:x[0])
# print(next[0][0])

