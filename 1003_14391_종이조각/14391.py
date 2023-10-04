# 20:01 ~  20:17
# 
# 입출력)
#  일단 입출력이 4이기 떄문에 완탐은 가능할듯하다
# 
# 문제)
#  위에 예제는 낚시인가..? 
#  거의 무조건 최댓값은 일직선으로 쭉 자른 값들의 합이 아닌가..?
#  반례 가능성) 
#    앞에 0 이 온다면..? 
# 
# 

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(input()))

row_total = 0
for a in range(len(graph)):
    tmp = int("".join(graph[a]))
    row_total += tmp
    
column_total = 0
for a in range(len(graph[0])):
    q = []
    for b in range(len(graph)):
        q.append(graph[b][a])
    tmp2 = int("".join(q))
    column_total += tmp2

answer = max(row_total, column_total)
print(answer)




