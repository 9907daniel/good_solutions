#
# 10:16 ~ 
#
# 쿼리의 최댓값이 100,000 이기 떄문에 
#
#
# 1   2  3  4  5  6  7 
# 24 25 26 27 28 29  8
# 23 40 41 42 43 30  9
# 22 39 48 49 44 31 10
# 21 38 47 46 45 32 11
# 20 37 36 35 34 33 12
# 19 18 17 16 15 14 13
#

q = int(input())

query = []
for _ in range(q):
    query.append(list(map(int, input().split())))


def snail(n, angle, graph, depth, count):
    if angle = 1:
       for a in range(n-1):
            graph[depth][a]
        
    
    
    
    
    
    pass



results = []

for a in range(len(query)):
    if query[a][0] == 1:
        n,x,y= query[a][1], query[a][2],query[a][3]
        graph = [[0]*n for _ in range(n)]
        snail(n, 1, graph, 0)










