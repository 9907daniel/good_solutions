# 10:10 ~ 
# 
# 입출력 : 100,000
#
# 배열 반대로 가면서 값이 더 작다면 추가를 하고, 아니면 스택을 비우고 삽입하는게..?
#
# 풀이 1) 반대로 탐색
# 3 2 3 2 1
# 0
# [3] -> 1
# [3,2] => []
#
# 
# 풀이 2) 정식으로
# -> 결국에는 정석적인 완탐으로 풀이가 되는데.. 이게 정해지는 기준이 지
# 잘 모르겠네..
#
#
#

from collections import deque

def solution(prices):
    results = []
    
    for a in range(len(prices)-1):
        count = 1
        for b in range(a+1,len(prices)-1):            
            if prices[b] >= prices[a]:
                count += 1
            else:
                break
        results.append(count)
    results.append(0)
    
    return results    
    
    
    
    
    
#     # 각 인덱스의 값을 저장하는 배열
#     results = []
    
#     # iterate
#     for a in range(len(prices)):
#         # 자신보다 큰 숫자 찾기의 count
#         count = 1
#         for c in range(a+1, len(prices)):
#             if prices[c] < prices[a] or c == len(prices)-1:
#                 results.append(count)
#                 break
#             elif prices[c] >= prices[a] :
#                 count += 1
                
#     results.append(0)
# return results
            
            
            
            
    