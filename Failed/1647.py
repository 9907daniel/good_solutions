# 13:38 ~ 13:48
# 
#
#
#
#
#
n, m = map(int, input().split())

graph = [[]*(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append(c)
    graph[b].append(c)







