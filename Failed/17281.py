# 19:56~32
#
# 이닝 수 : 50
# 사람 수 : 9
#
# 
#
#
# 1) 스택 / 큐로 순서를 기록하애 할꺼 같다 
# 
# if == 4: 
#   score += len(stack) -> 
# 
# if == 3:
#   if move all -> +3 -> if not 0 -> 
#
#
# 50 * 8! * 8
#

from collections import deque
from itertools import permutations

n = int(input())
highest_score = 0

orders = []

for _ in range(n):
    orders.append(list(map(int, input().split())))

# 0~8
tmp = [a for a in range(9)]
# 3
l = [tmp[3]]
tmp.pop(3)

visited = []

# 1~9 까지 4번은 고정으로 하고 모든 조합을 구한다
for a in permutations(tmp, len(tmp)):
    if a not in visited:
        visited.append(a)
        l = [tmp[3]]
        for b in range(len(a)):
            l.append(a[b])

    ###############################
        q = deque([0,0,0])
        out = 0
        score = 0
        start = 0
        
        # print(a)
        
        # for c in range(len(orders)):
        #     current = []
        #     for d in range(len(l)):
        #         current.append(orders[c][l[d]])
            
        #     print(current)
            
            
        #     while True:
        #         if start >= len(curre):
        #             start = 0
                
        #         if l[start] == 4:
        #             score += 1
        #             for a in range(len(q)):
        #                 tmp = q.popleft()
        #                 if tmp != 0:
        #                     score += 1
        #                 q.append(0)
        #         elif l[start] == 1:
        #             x = q.popleft()
        #             if x != 0:
        #                 score += 1
        #             q.append(l[start])
        #         elif l[start] == 2:
        #             for a in range(2):
        #                 x = q.popleft()
        #                 if x != 0:
        #                     score += 1
        #                 if a == 0:
        #                     q.append(l[start])
        #                 else:
        #                     q.append(0)
        #         elif l[start] == 3:
        #             for a in range(3):
        #                 x = q.popleft()
        #                 if x != 0:
        #                     score += 1
        #                 if a == 0:
        #                     q.append(l[start])
        #                 else:
        #                     q.append(0)
        #         start += 1
        #         if l[start] == 0:
        #             out += 1
        #             if out == 3:
        #                 break
            
        #     start += 1
        #     if start >= len(l):
        #         start = 0

        # print(score)

        
        
            
    
    
    
    










# score = 0
# start = 0

# for a in range(n):
#     l = list(map(int, input().split()))
#     q = deque([0,0,0])
#     out = 0
    
#     l.sort()
    
#     while True:
#         if start >= len(l):
#             start = 0
        
#         if l[start] == 4:
#             score += 1
#             for a in range(len(q)):
#                 tmp = q.popleft()
#                 if tmp != 0:
#                     score += 1
#                 q.append(0)
#         elif l[start] == 1:
#             x = q.popleft()
#             if x != 0:
#                 score += 1
#             q.append(l[start])
#         elif l[start] == 2:
#             for a in range(2):
#                 x = q.popleft()
#                 if x != 0:
#                     score += 1
#                 if a == 0:
#                     q.append(l[start])
#                 else:
#                     q.append(0)
#         elif l[start] == 3:
#             for a in range(3):
#                 x = q.popleft()
#                 if x != 0:
#                     score += 1
#                 if a == 0:
#                     q.append(l[start])
#                 else:
#                     q.append(0)
#         start += 1
#         if l[start] == 0:
#             out += 1
#             if out == 3:
#                 break
    
#     start += 1
#     if start >= len(l):
#         start = 0

# print(score)






