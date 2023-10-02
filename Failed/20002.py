# 08:16 ~ 
# 
# 입출력 : N = 300
# 300 + 299*4
#
# 완탐, DFS, 백트래킹은 힘들수도 있을꺼 같다..
# -> DP, BFS..? 누적합..? 
#
# 1) 모든 kxk 좋방으로 돌아야한다.. 
# 
# i) 일단 BFS..
#
#

n = int(input())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

current_max = -1001

for a in range(n):
    for b in range(n):
        current_max = max(current_max, graph[a][b])











# for a in range(n):
#     for b in range(n):
#         # 현재 == graph[a][b]
#         current_sum = graph[a][b]
#         for c in range(1,n-max(a,b)):
#             for d in range(a,a+c+1):
#                 current_sum += graph[d][b+c]
#             current_sum += sum(graph[a+c][b:b+c+1])
#             print(a,b)
#             print(current_sum)
#             current_max = max(current_max, current_sum)
        
# print(current_max)
                

## 완탐 풀이

# for a in range(1, n):
#     for b in range(n-a):
#         if b+a < n:
#             for c in range(n-a):
#                 tmp = 0     
#                 if c+a < n:
#                     for d in range(b,b+a+1):
#                         if c+a != n-1:
#                             tmp += sum(graph[d][c:c+a+1])
#                         else:
#                             tmp += sum(graph[d][c:c+a+1])    
#                     current_max = max(current_max,tmp)    

# print(current_max)
                
# 입출력 : 300*300*300*300 = 90000*300 = 2,700,000







