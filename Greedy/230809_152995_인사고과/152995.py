# 09:18 ~ 10:08 + 10:41 ~ 11:18
#
# 알고리즘 : 그리디
#
# 비슷한 유형 : 백준 - 신입사원
#
# i) 한번 iterate를 통해 둘다 낮은 사람들은 제거 후에 합으로 다시 재정렬하자
# 시간초과를 줄여야한다..

def solution(scores):
    wonhoe = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    before = 0
    total = sum(wonhoe)

    count = 1
    for score in scores:
        if wonhoe[0] < score[0] and wonhoe[1] < score[1]:
            return -1
        if before <= score[1]:
            
            if total < score[0]+ score[1]:
                count += 1
            before = score[1]
    
    return count
        
        

# def solution(scores):
#     wonhoe = scores[0]
    
#     scores.sort(key= lambda x:(-x[0],-x[1]))
    
#     candidates = [scores[0]]
#     dic = {}
#     dic[scores[0][0]] = scores[0][1]
    
#     for a in range(1, len(scores)):
#         broken = False
#         for b in dic:
#             if scores[a][0] != b and scores[a][1] < dic[b]:
#                 broken = True
#                 break
#         if broken != True:
#             if scores[a][0] not in dic:
#                 dic[scores[a][0]] = scores[a][1]
#             candidates.append(scores[a])
            
#     candidates.sort(key=lambda x:(x[0]+x[1]), reverse = True)
#     ranking = [0]*len(candidates)
#     ranking[0] = 1
    
#     start = 1
#     current = 1
#     tmp = 1
    
#     while start < len(ranking):
#         if sum(candidates[start]) != sum(candidates[start-1]):
#             current += tmp
#             ranking[start] = current
#             tmp = 1
#         else:
#             tmp += 1
#             ranking[start] = current
#         start += 1
  
#     if wonhoe in candidates:
#         return ranking[candidates.index(wonhoe)]
#     return -1
