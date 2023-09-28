# # 22:51 ~  
# # 
# # 
# # 19 20 17 18 15 16 13 14 11 12
# #
# # 1) 20 19 17 18 15 16 13 14 11 12
# # 2) 20 19 18 17 15 16 13 14 11 12
# # 3) 20 19 18 17 16 15 13 14 11 12
# # 4) 20 19 18 17 16 15 14 13 11 12
# #
# #
# #
# # 문제)
# # S 가 살아있는동안, 매순간의 보이는 비정렬을-정렬해준다
# # 하지만 정렬된거에서 한번 더 정렬을 하는것이 더 최적이라면..? 
# #
# # 50 * 1,000,000 = 50,000,000
# # -> 매번 iterate를 해주기 보다, stack을 유지하며 끼워 맞춰주는거는 어떨까?
# #
# #
# #
# # 맨 앞에 정렬이 가장 '뒷선'이 맞나?
# #


















# from copy import deepcopy
# import sys

# n = int(input())
# l = list(map(int, input().split()))
# s = int(input())

# if n == 1:
#     print(*l)
#     sys.exit()
# if n == 2 and s != 0:
#     l.sort()
#     print(*l)
#     sys.exit()


# compare = deepcopy(l)
# compare.sort(reverse = True)
# count = 0

# while count < s:
#     for a in range(1, len(l)):
#         additive = 0
#         for b in range(a-1,-1,-1):
#             if compare == l:
#                 print(*l)
#                 sys.exit()
                
#             if l[a] < l[b]:
#                 if additive != 0:
#                     tmp = l[a]
#                     l[a] = l[b+1]
#                     l[b+1] = tmp
#                 break
#             else:
#                 additive += 1
            
#             if b == 0:
#                 if l[a] > l[b]:
#                     tmp = l[a]
#                     l[a] = l[b]
#                     l[b] = tmp
            
#             if count+additive > s:
#                 print(*l)
#                 sys.exit()
#         count += additive
# print(*l)



