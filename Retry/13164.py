# 10:16
# 
# 입출력 : 30만 -> 최대 nlogn
# 
# 
# 
# 
# 
# 
# 예시) -> 5명을 3개의 팀으로 나눈다
# 5 3 
# 1 3 5 6 10
# ___ ___ _  -> 3
# 
# 0 2 4 5 9
#
# 풀이) 그리디라고 생각했지만 매게변수 탐색이 더 좋을꺼 같다
# start = 1~10 = 5
# 5를 넘는다면..
# -> TLE 걸리나..? 
# -> 완전 필요 없는 사람들 또한 있기 때문에 Nope
#
# 2 2 1 4
# 4 2 2 1
#
#

from collections import deque

n, k = map(int, input().split())

l = list(map(int, input().split()))

difference = []
for a in range(1,len(l)):
    difference.append(l[a]-l[a-1])
    
difference.sort(reverse = True)
difference = deque(difference)

for _ in range(k-1):
    difference.popleft()

print(sum(difference))














# start = l[0]
# end = l[n]-1
# answer = 1e8
# while start <= end:
#     # 현재 target
#     mid = (start + end)//2
    
#     groups_formed, current_group_start = 0, l[0]
#     tmp = [l[0]]
#     total = 0
    
#     for a in range(1, len(l)):
#         if l[a]-l[0] > mid:
#             groups_formed += 1
#             total
#             if groups_formed >= k:
#                 end = mid-1
#                 break
#             else:
#                 current_group_start = l[a]
#         elif a == len(l)-1:
#             groups_formed += 1
            
            
            
#     if groups_formed < k:
#         start = mid+1
    
    












