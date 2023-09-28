# 12:18 ~ 

from copy import deepcopy

def check(visited, a, b, n, graph):
    tmp = deepcopy(visited)
    for c in range(n):
        if graph[a][c] == True and c != b:
            return False, tmp
        visited[a][c] = True
    
    for c in range(n):
        if graph[c][b] == True and c != a:
            return False, tmp
        visited[c][b] = True

    count = 0
    while a+count < n and b+count < n:
        if graph[a+count][b+count] == True and count != 0:
            return False, tmp
        visited[a+count][b+count] = True
        count += 1
        
    count = 0
    while 0<=a-count and 0<=b-count:
        if graph[a-count][b-count] == True and count != 0:
            return False, tmp
        visited[a-count][b-count] = True
        count += 1
        
    count = 0
    while 0<=a-count and b+count < n:
        if graph[a-count][b+count] == True and count != 0:
            return False, tmp
        visited[a-count][b+count] = True
        count += 1

    count = 0
    while a+count<n and 0<=b-count:
        if graph[a+count][b-count] == True and count != 0:
            return False, tmp
        visited[a+count][b-count] = True
        count += 1
    
    # print(visited)
    return True, visited


answer = 0
tempo = []
record = []
def combinations(graph, visited, count, n):
    global answer
    global tempo
    if count == n-1:
        tempo.sort()
        if tempo not in record:        
            answer += 1
            record.append(tempo)
        return
    
    for a in range(n):
        for b in range(n):
            if visited[a][b] != True and graph[a][b] != True:
                tmp = deepcopy(visited)
                possible, visited = check(visited, a,b,n, graph)
                if possible:
                    graph[a][b] =True
                    tempo.append([a,b])
                    combinations(graph,visited, count+1, n)
                    graph[a][b] = False
                    tempo.pop()
                visited = tmp
            
n = int(input())

graph = [[False]*n for _ in range(n)]
visited = [[False]*n for _ in range(n)]

# check(visited, 3, 2, n, graph)



combinations(graph, visited, 0, n)

print(answer)

[[False, False, True, False, False, True, False, False],
 [True, False, True, False, True, False, False, False],
 [False, True, True, True, False, False, False, False], 
 [True, True, True, True, True, True, True, True],
 [False, True, True, True, False, False, False, False],
 [True, False, True, False, True, False, False, False], 
 [False, False, True, False, False, True, False, False], 
 [False, False, True, False, False, False, True, False]]




[[True, True, True, True, True, True, True, True],
 [True, True, False, False, False, False, False, False], 
 [True, False, True, False, False, False, False, False], 
 [True, False, False, True, False, False, False, False],
 [True, False, False, False, True, False, False, False],
 [True, False, False, False, False, True, False, False],
 [True, False, False, False, False, False, True, False], 
 [True, False, False, False, False, False, False, True]]

[[True, True, True, True, True, True, True, True],
 [True, True, True, True, True, True, True, True], 
 [True, True, True, True, False, False, False, False],
 [True, False, True, True, True, False, False, False],
 [True, False, True, False, True, True, False, False], 
 [True, False, True, False, False, True, True, False], 
 [True, False, True, False, False, False, True, True], 
 [True, False, True, False, False, False, False, True]]