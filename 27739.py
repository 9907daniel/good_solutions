# 13:39 ~ 14:52
#
# 입력 : 2000..
#
# <문제>
#  2 1 5 3 4
#  2 1 5     -> 5 1 2 3 4  == 4
#    1 5 3   -> 
#      5 3 4 -> 3,4,5
# 
# 1 2 3 4
# 1 3 4 
# <풀이법..>
# - 고려 할 상황이 두개가 있을드사핟
# 1) 정렬을 하고 다음꺼에 이어지는게 있는지 확인
# 2) reverse 정렬을 하고 반대로 확인해준다
#
# 반례) 자유 정렬을 하지 않은 l,r 에서 최대가 있을때
#
#
# 시간초과 나는 이유 : 자유 배열을 모든 조합으로 구해서

n,k = map(int, input().split())
l = list(map(int, input().split()))

consecutive = 0
for a in range(n-k+1):
    current = l[a:a+k]
    current.sort()
    dic = {}
    for b in current:
        dic[b] = 1
            
    # for c in range(len(current)):
    #     start_count = 1
    #     okok = current[c]
    #     for d in range(c+1, len(current)):
    #         if current[d] == okok+1:
    #             start_count += 1
    #             okok = current[d]
    #         else:
    #             break
    #     consecutive = max(consecutive, start_count)
    
    if a != 0 and a != n-k:
        # left, right, mid로 나눴다
        left = l[:a]
        right = l[a+k:]  
                    
        # 왼쪽을 기준으로 확인
        count = 0
        rn = left[-1]
        for b in range(len(left)-2,-1,-1):
            if left[b] == rn -1:
                rn = b
                count += 1
            else:
                break
        consecutive = max(consecutive, count)

        check_all = 0
        while True:
            if rn+1 in dic:
                count += 1
                rn += 1
                check_all += 1
            else:
                break
        if check_all == len(dic):
            for c in range(len(right)):
                if right[c] == rn+1:
                    rn += 1
                    count += 1
                else:
                    break
        consecutive = max(consecutive, count)

        # 오른쪽을 기준으로 확인
        count = 0
        rn = right[0]
        for b in range(len(right)):
            if right[b] == rn+1:
                rn += 1
                count +=1
            else:
                break
        consecutive = max(consecutive, count)
    
        
        rn = right[0]
        while True:
            if rn-1 in dic:
                rn = rn-1
                count +=1
            else:
                break
        consecutive = max(consecutive, count)  
            
    elif a == 0:
        right = l[a+k:]
        count = 1
        rn = right[0]
        for b in range(1,len(right)):
            if right[b] == rn+1:
                rn += 1
                count +=1
            else:
                break
        consecutive = max(consecutive, count)
    
        rn = right[0]
        while True:
            if rn-1 in dic:
                rn = rn-1
                count +=1
            else:
                break
        consecutive = max(consecutive, count)        
        
        
        
    elif a == n-k:
        left = l[:a]
        current = l[a:]
        count = 1
        rn = left[-1]
        for b in range(len(left)-2,-1,-1):
            if left[b] == rn -1:
                rn = b
                count += 1
            else:
                break
        consecutive = max(consecutive, count)

        while True:
            if rn+1 in dic:
                count += 1
                rn += 1
                check_all += 1
            else:
                break
        consecutive = max(consecutive, count)
              
print(consecutive)      
            
            
            
            
            
            
        
        
        # 1) 왼쪽과 비교를 했을때 왼쪽이 정렬되어 있는지 확인 (reverse or not reverse)
        # for b in range(len(left)):
        #     rn = b
        #     count = 0
        #     for c in range(b+1, len(left)):
        #         if left[c] == left[rn]+1:
        #             rn = c
        #             count += 1
        #         else:
        #             consecutive = max(consecutive, count)
        #             break
        #         if rn == c:
        # if rn == len(left)-1
        
        
        
        
        
        
#         current.sort()
#         combine = current + right
#         print(combine)
#         for b in range(len(combine)):
#             count = 0
#             rn = combine[b]
#             for c in range(b+1, len(combine)):
#                 if combine[c] == rn+1:
#                     rn = combine[c]
#                     count += 1
#                 else:
#                     break
#             consecutive = max(consecutive, count)
        
#         current.sort(reverse = True)
#         combine2 = left + current
#         # print(combine2)
#         for b in range(len(combine2)-1,-1,-1):
#             count = 0
#             rn = combine2[b]
#             for c in range(b, -1, -1):
#                 if combine2[c] == rn+1:
#                     rn = combine2[c]
#                     count += 1
#                 else:
#                     break 
#             consecutive = max(consecutive, count)
     
#     elif a == 0:
#         current = l[:a+k]
#         right = l[a+k:]
#         current.sort()
#         combine = current + right
#         for b in range(len(combine)):
#             count = 0
#             rn = combine[b]
#             for c in range(b+1, len(combine)):
#                 if combine[c] == rn+1:
#                     rn = combine[c]
#                     count += 1
#                 else:
#                     break
#             consecutive = max(consecutive, count)

#     elif a == n-k:
#         left = l[:a]
#         current = l[a:]

#         current.sort(reverse = True)
#         combine2 = left + current
#         for b in range(len(combine2)-1,-1,-1):
#             count = 0
#             rn = combine2[b]
#             for c in range(b, -1, -1):
#                 if combine2[c] == rn+1:
#                     rn = combine2[c]
#                     count += 1
#                 else:
#                     break 
#             consecutive = max(consecutive, count)

# print(consecutive)