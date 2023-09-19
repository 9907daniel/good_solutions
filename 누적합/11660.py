n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
orders = []

for _ in range(m):
    orders.append(list(map(int, input().split())))
    
added = [[0]*n for _ in range(n)]

for a in range(n):
    for b in range(n):
        if a == 0 and b == 0:
            added[a][b] = graph[a][b]
        elif a == 0:
            added[a][b] = graph[a][b]+added[a][b-1]
        elif b == 0:
            added[a][b] = graph[a][b]+added[a-1][b]
        else:
            added[a][b] = graph[a][b]+added[a-1][b]+added[a][b-1]-added[a-1][b-1]

print(graph)

answers = []
for a in range(len(orders)):
    current = orders[a]
    if current[0] > 1 and current[1] > 1:
        print(added[current[2]-1][current[3]-1], added[current[0]-1][current[3]-1], added[current[2]-1][current[1]-1], added[current[0]-1][current[1]-1])
        answers.append(added[current[2]-1][current[3]-1]-added[current[0]-2][current[3]-1]-added[current[2]-1][current[1]-2] + added[current[0]-2][current[1]-2])
    elif current[0] > 1:
       answers.append(added[current[2]-1][current[3]-1]-added[current[2]-1][current[1]-2])
    elif current[1] > 1:
        answers.append(added[current[2]-1][current[3]-1]-added[current[0]-2][current[3]-1])
    else:
        answers.append(added[current[2]-1][current[3]-1])

# for a in answers:
#     print(a)
