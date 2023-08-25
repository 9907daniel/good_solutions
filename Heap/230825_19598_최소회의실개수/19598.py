# 10:40 ~ 11:13 (33분)
# 
# 문제 : N개의 회의를 최소로 분배하라
#
# 시간 복잡도 : 10만 -> NLogN 까지 가능
# 
# 알고리즘 : 그리디 + 자료구조 (큐 / 힙) + 정렬
# 
# 
# 1) 모든 입력값을 받는다
# 2) 시작하는 시간을 기준으로 정렬을 한다 
#   0 40
#   5 10
#   15 30
#
# 3) 각 stack를 순회하면서, 끝나는 시간만을 추가한다
# 
# 4) 여러 stack가 있다면 순차적으로 iterate를 하고, 최소값순으로 꺼내면서 강의실에 끝나는 시간을 update
#
# heappop = 기본적으로 최소값부터 나온다 (이미 정렬이 되어 있기 때문에 최소 최소만 비교해주면 된다.)
#                                 즉, 햔제 기징 작은값으로 가장 빨리 시작하는 미팅 시간을 채워줘야한다

from heapq import heappush, heappop

n = int(input())

timeslots = []

for _ in range(n):
    timeslots.append(list(map(int, input().split())))
    
timeslots.sort(key=lambda x:x[0])

stack = []

for a in range(len(timeslots)):
    if len(stack) == 0:
        heappush(stack, timeslots[a][1])
    
    else:
        x = heappop(stack)
        if timeslots[a][0] >= x:
            heappush(stack, timeslots[a][1])
        else:
            heappush(stack, x)
            heappush(stack, timeslots[a][1])

print(len(stack))


        # for b in range(len(stack)):
        #     tmp = -stack[b]
        #     if tmp > timeslots[a][0] and b == len(stack)-1:
        #         heappush(stack, -timeslots[a][1])
        #     elif tmp <= timeslots[a][0]:
        #         stack.pop(b)
        #         heappush(stack, -timeslots[a][1])
        #         break
                
    

    


