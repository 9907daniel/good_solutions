from copy import deepcopy

n,m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
    
next = [graph]
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
    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)
    tmp2 = deepcopy(graph)
    tmp3 = deepcopy(graph)
    
    # 남
    x = south(tmp,a,b)
    next.append(x)
    
    # 북
    x = north(tmp1,a,b)
    next.append(x)
    
    # 동
    x = east(tmp2,a,b)
    next.append(x)
    
    # 서
    x = west(tmp3,a,b)
    next.append(x)

    return next

def camera_two(graph, a, b, next):
    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)

    # 남북
    x = south(tmp,a,b)
    x = north(tmp,a,b)
    next.append(x)
        
    # 북
    y = east(tmp1,a,b)
    y = west(y,a,b)
    next.append(y)

    return next

def camera_three(graph, a, b, next):
    tmp = deepcopy(graph)
    tmp1 = deepcopy(graph)
    tmp2 = deepcopy(graph)
    tmp3 = deepcopy(graph)

    # 북동
    x = north(tmp,a,b)
    x = east(x,a,b)
    next.append(x)
        
    # 동남
    y = east(tmp1,a,b)
    y = south(y,a,b)
    next.append(y)   
 
    
    # 남서
    y = south(tmp2,a,b)
    y = west(y,a,b)
    next.append(y)  
    
    # 서북
    y = west(tmp3,a,b)
    y = north(y,a,b)
    next.append(y)  
    
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
    next.append(x)
        
    # 동남북
    y = east(tmp1,a,b)
    y = south(y,a,b)
    y = north(y,a,b)
    next.append(y) 
   
    
    # 남서동
    y = south(tmp2,a,b)
    y = west(y,a,b)
    y = east(y,a,b)
    next.append(y)  
    
    # 서북남
    y = west(tmp3,a,b)
    y = north(y,a,b)
    y = south(y,a,b)
    next.append(y)

    return next
    
def camera_five(graph, a, b,next):
    global current_min

    tmp = deepcopy(graph)

    # 북동서남
    x = north(tmp,a,b)
    x = east(x,a,b)
    x = west(x,a,b)
    x = south(x,a,b)

    next.append(x)

    return next


gg = []
for a in range(n):
    for b in range(m):
        if graph[a][b] == 1 or graph[a][b] == 2 or graph[a][b] == 3 or graph[a][b] == 4 or graph[a][b] == 5:
            gg.append(graph[a][b], a, b)

# [4,4,1],[3,2,1] ....
def dfs(gg, current, graph):
    if current == len(gg):
        return
    
    if gg[current][0] == 1:
        graph = camera_one(gg[current],gg[current][1],gg[current][2])
        dfs(gg, current+1, graph)
        
        
        
        
        
    elif graph[a][b] == 2:
        next = camera_two(l[c],a,b,next)

    elif graph[a][b] == 3:
        next = camera_three(l[c],a,b,next)

    elif graph[a][b] == 4:
        next = camera_four(l[c],a,b,next)

    elif graph[a][b] == 5:
        next = camera_five(l[c],a,b,next)


dfs(gg, 0)
            
        



current_min = 1e7
for a in next:
    count = 0
    for b in range(len(a)):
        for c in range(len(a[b])):
            if a[b][c] == 0:
                count += 1
    current_min = min(current_min, count)

print(current_min)


