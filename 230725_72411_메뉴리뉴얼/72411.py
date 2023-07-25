# 09:44 ~ 10:33
#
# 입력값 낮음 
#
# 알고리즘 : 완탐
# if current compare in one of the other lists -> append
#

from itertools import combinations 

def solution(orders, course):

    
    
    results = []
    dic = {}
    already_compared = []
    
    for a in range(len(orders)):
        # 비교할 음식 대상
        tmp = list(orders[a])
        
        # 비교 할 음식 대상의 조합들
        for c in range(2, len(tmp)+1):
            # 만약 코스 길이 [2,3,4] 안에 있다면 좋압을 구해라
            if c in course:
                for d in combinations(tmp, c):
                    if d not in already_compared:
                        # 비교할 조합
                        comparing_food = list(d)
                        comparing_food.sort()

                        for b in range(len(orders)):
                            compare = list(orders[b])
                            common_menu = []

                            # 자기 자신은 비교하지 마
                            if b != a:
                                for e in range(len(comparing_food)):
                                    if comparing_food[e] in compare:
                                        common_menu.append(comparing_food[e])
                                    else:
                                        break
                            if len(common_menu) == len(comparing_food):
                                
                                x = "".join(comparing_food)
                                if x in dic:
                                    dic[x] += 1
                                else:
                                    dic[x] = 1
                        already_compared.append(str(comparing_food))
    
    answer = [0]*11
    for a in dic:
        answer[len(a)] = max(answer[len(a)], dic[a])
    
    final_answer = []
    
    for a in dic:
        if dic[a] == answer[len(a)]:
            final_answer.append(a)
            
    final_answer.sort()
    return final_answer
        
        
        
        
        