# 21:59 ~ 22:30
# 
# 문제 요점 : 최대한 늦게 시작을 하면서 모든 작업은 끝내기 
# 즉, 마감시간에 맞춰 시작을 하는게 최적이다
#
# 문제 예제를 풀어보자)
# 3 5
# 8 14
# 1 16
# 5 20
#
# 1) 3시간짜리 작업을 5시 까지 끝내기 위해 2시에 시작을 한다
# 2) 8시간짜리 작업을 14시 까지 끝내기 위해 6시에 시작을 한다
# 3) 1시간짜리 작업을 16시 까지 15시에 시작을 한다
# 4) 5시간짜리 작업을 20시 까지 끝내가 위해 5시에 시작한다
#
# 1) current wake_up = 2, current_last_time = 5
# 
# iterate하면서 만약 현재 작업을 시작해야 하는 시간이 current_last 보다 작다면, 그만큼 더 일찍 일어난다
# 시간들도 최산화 
#
# 입출력)
# 1000*1000*1000 = 1,000,000,000
# 가능 알고리즘 : DP, 그리디, 이진탐색, ... -> 그리디
#
# 반례를 생각하는게 조금.. -> 그려보는게 좋았을꺼 같아..
#

import sys

n = int(input())
works = []
for _ in range(n):
    works.append(list(map(int, input().split())))

works.sort(key=lambda x:x[1])

earliest = works[0][1]-works[0][0]
finish_time = works[0][1]

for a in range(len(works)):
    testing = works[a][1]-works[a][0]
    if testing < 0:
        print(-1)
        sys.exit()
        
# 3 5 -> 일어나 = 2, 끝나는 시간 = 5
# 8 12 -> 일어나 = 1, 끝나는 시간  = 13

for a in range(1, len(works)):
    # 4
    tmp = works[a][1]-works[a][0]
    
    # 더 일찍일어나야한다면..
    if tmp < finish_time:
        earliest -= finish_time-tmp
        finish_time = works[a][1]
    else:
        finish_time += works[a][0]
    
    if earliest < 0:
        print(-1)
        sys.exit()
        
print(earliest)    