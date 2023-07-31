#
# 09:36 ~ 10:37 + 10:51 ~ 11:02
#
# 각 사람들에게 최소가 되는거리에 우체국을 세우기
#
#
# 입력 : 10만.. 변수 1억..? 수상
#
#
#
# -----------------
# 1) 1번째 말을은 1에 위치하며 3명이 산다
# 2) 2번째 마을은 2에 위치하며 5명이 산다
# 3) 3번째 마을은 3에 위치하며 3명이 산다
#
# 3 5 3
# 1*3 + 0*5 + 1*3 = 6 => 최소
#
#
# 풀이 1) 약간의 가지치기로 On^2가 가능할수도 있지만 변수값이 최대 1억인게 걸린다..
#
# -> 아니다.. 위치가 x[i]이면 거기까지의 배열을 만들어야해 절대 안된다..
#
#
#####################################################

n = int(input())

graph = []
total = 0
for a in range(n):
    graph.append(list(map(int, input().split())))
    total += graph[a][1]

# 아무 순서가 가능하니 정렬을 해주자..?
graph.sort(key=lambda x:x[0])

# n =1일때는 비교 불가
if n == 1:
    print(1)
else:
    # 총 사람을 구해본다
    #
    # 1 1 1 1 3 -> 7 -> 3
    #
    count = 0
    for a in range(len(graph)):
        count += graph[a][1]
        if count >= total/2:
            stop_point = graph[a+1][0]
            break
    print(stop_point)
    #         right = total-count
    #         left = total-count-graph[a][1]
    #         break
    # print(left, right)
    # if right < left:
    #     print(graph[stop_point][0]+1)
    # elif right > left:
    #     print(graph[stop_point-1][0]+1)




#####################################################
#####################################################
#####################################################

# 풀이 2) 평균을 구하면되지 안을까?? 직접 계산할 필요는 없다 -> 1억
#
# 1 1 1 1 3
#
# 2 1 0 1 6 = 10
#
# 3 2 1 0 3 = 9
# 4 3 2 1 0 = 10
#
# abs 를 활용하는데 전부 음수다. -> 사용하면 안된다
# 음수면 -1을 해줘야한다..
#

#
import math 
n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

if n == 1:
    print(1)
else:
    total = 0
    total_people = 0
    for a in range(len(graph)):
        # 평균적으로 사람들이 사는곳에 만드는게 맞다 -> 꼭 집이 없어도 된다 (우체국 위치에)
        total += (graph[a][0]*graph[a][1])
        total_people += graph[a][1]

    x = (total / total_people)
    # 만약 소수쪽이 .5면 -1을 더해야한다
    
    if x >= 0:
        print(round(x))
    else:
        if x - math.floor(x) == 0.5:
            print((-(round(abs(x)))-1))
        else:
            print(round(x))
    
#####################################################
#####################################################
#####################################################

# # 풀이 1) 하나의 마을을 기준점으로 잡고 abs 계산

# n = int(input())

# graph = []
# for _ in range(n):
#     graph.append(list(map(int, input().split())))

# answer = []
# for a in range(len(graph)):
#     current_point = graph[a][0]
#     total_distance = 0
    
#     for b in range(len(graph)):
#         total_distance += abs(graph[b][0]-graph[a][0])*graph[b][1]
    
#     answer.append([total_distance, a])

# answer.sort(key=lambda x:(x[0],x[1]))
# print(answer[0][1]+1)
    





