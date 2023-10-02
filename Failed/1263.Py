# 08:09 ~ 08:56
# 
# T 시간이 걸리고, 마가시간은 S시간이다
# 
# current = 2 이다
# 3 5 -> 2
# 8 14 -> 6
# 1 16 -> 15
# 5 20 -> 15
#
# **만약 초과를 한다면 그 초과하는 시간만큼 낮잠을 앞당겨주고, 0 미만으로 내려간다면 -1
# current = 2, finish time = 5
# if 6 > 5 -> else : current - (difference) -> if -1 -> -1
#   current = 2 finish time = 5+8 -> 13 
# if 15 > 13 
#   current = 2 finish time = 13+1 -> 14
# if 15 > 14
#   current = 2 finisht time = 14+5 -> 19
# 
#
# 반례)
# 4 5 -> 1          -> 1시에 시작해서 5시에 끝내기
# 10 20 -> 10       -> 5시에 시작해서 15시에 끝내기
# 4 15  -> 11       -> 초과를 한다 : 1시 - (15-11)-> -1
#
# 현재 시간은 15시이고, 5시간짜리 작업을 하는데, 최소 13시에 시작해서~ 18시까지 끝내야한다
# 지금 구현 : 현대시간 15시 - 작업을 잔행하는 시간(5) = 10으로 하게 하고 잇다..
# 하지만 여기서...
# 공백기는 더해줘야한다 15-13 -> 두시간만 뺴주면 된다...? 
#
#
# 4 5 -> 시작 시간 = 1 + 현재 시각 5
# 4 15 -> 시작 시간 = 0 + 현재 시각 20
# 10 20 -> 
#
#
# #
import sys

n = int(input())
l = []
for _ in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x:x[1])



# import sys

# n = int(input())
# l = []
# for _ in range(n):
#     l.append(list(map(int, input().split())))

# # 작업이 끝나는 순대로 정렬하기 
# # l.sort(key=lambda x: ((x[1]-x[0]),x[0]))
# l.sort(key=lambda x:x[1])

# # 시작시간은 작업 최대 끝나는 시간 - 걸리는 시간 = 가장 늑제 시작할때 이때 시작한다
# current = l[0][1]-l[0][0]

# # 가장 늦게 끝난 시간
# current_finish = l[0][1]

# print(l)
# for a in range(1, len(l)):
#     print(current, current_finish)
#     # 만약 현재 가장 늦게 시작해도 괜찮은 시간이 전 작업 중 가장 늦게 끝난 시간보다 크다면 괜찮다!
#     if l[a][1]-l[a][0] >= current_finish:
#         current_finish += l[a][0]
#     else:
#         # 아니라면 전체 시간을 그 차이만큼 앞당겨줘야한다
#         if current - (current_finish-(l[a][1]-l[a][0])) >= 0:
#             current = current - (current_finish-(l[a][1]-l[a][0]))
#         # 앞당기는데 0 밑으로 간다면 부가능한 작업이다
#         else:
#             print(-1)
#             sys.exit()
#     print(current, current_finish)

# print(current)
         
# 4 -> 5
#
#
#



