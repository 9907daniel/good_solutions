# 10:53 ~ 11:09
# 
# 입력값 : 20 * 100,000 -> 하나의 for문으로..
#
#
# 1 4 
# 2 3
# 3 2
# 4 1
# 5 5
#
#
# 1) iterate를 하면서 현대 2번째 면접 꼴등 재갱신을 한다
# 2) 만약 현재 지원자가 현재 면접 꼴등 보다 순위가 안좋다면 제외한다
# -> for 문 하나로 푸는 그리디
#

t = int(input())
results = []

for _ in range(t):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
        
    graph.sort(key=lambda x : (x[0],x[1]))
        
    # 서류 1등은 무조건 pass~ 
    # 시작 면접 꼴등은 서류 1등으로 초기화 시킨다
    current_last = graph[0][1]
    for a in range(1, len(graph)):
        if graph[a][1] > current_last:
            n -= 1
        current_last = min(current_last, graph[a][1])
    results.append(n)
    
for a in results:
    print(a)