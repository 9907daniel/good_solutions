# 15:10 ~ 15:49
#
# 입출력) 10,000 -> 대략 N^2 * logN 가능할듯하다
#
# 알고리즘) 빡구현일 확률이 높다 / DFS (노드 탐색)
#
# 순서)
# 1) refereall을 통해 관계를 형성해본다
# 2) seller을 탐색하는 동안 모든 referall node를 거치면서 각 부모에 값을 더해준다
# 3) 0.9를 곱한 값을 더해주는게 복잡할수도 있다..
#
# 자료구조)
# 해쉬맵을 사용할까..?
#

import math

def solution(enroll, referral, seller, amount):
    
    dic = {}
    recorded_next = {}
    for a in range(len(enroll)):
        dic[enroll[a]] = 0
        recorded_next[enroll[a]] = referral[a]

    for a in range(len(seller)):
        current = amount[a]*100
        
        sell_person = seller[a]
        
        # 여기 까지 효율화 시키니까 TLE 통과 -> 1,000,000,000 -> 100,000
        # for b in range(len(enroll)):
        #     if enroll[b] == sell_person:
        #         next_person = referral[b]
        next_person = recorded_next[sell_person]

        
        # 조심
        if current-(math.ceil(current*0.9)) < 1:
            dic[sell_person] += current
            current = 0
        else:
            dic[sell_person] += math.ceil(current*0.9)
            current = current - math.ceil(current*0.9)
    
        while True:
            if next_person == '-' or current <= 0:
                break
                
            if current-(math.ceil(current*0.9)) < 1:
                dic[next_person] += current
                current = 0
            else:
                dic[next_person] += math.ceil(current*0.9)
                current = current - math.ceil(current*0.9)
            
            # 다음 깊이 탐색 대상을 찾는 과정에서 TLE가 나왔다.. 
            # for c in range(len(enroll)):
            #     if enroll[c] == next_person:
            #         next_person = referral[c]
            next_person = recorded_next[next_person]

    answer = []
    for a in range(len(enroll)):
        current = dic[enroll[a]]
        answer.append(int(current))
                      
    return answer
