# 09:59
#
# 입력 : 1000 -> 1000*1000 = 100,000 -> 100,000*1000 -> 100,000,000
#
# 알고리즘 : DP / 트리(?) / 완탐..?
#
# 풀이 : 1명 이든, 10 명이든 1000명이든 최소값을 어떻게 구할까..?
#
# DP[100] 을 구하자
# 
#

target, city_num = map(int, input().split())

graph = []

for _ in range(city_num):
    graph.append(list(map(int, input().split())))
    
# 가성비 순대로 sort()
graph.sort(key=lambda x:(x[1]/x[0]), reverse = True)

for a in range(len(graph)):
    pass