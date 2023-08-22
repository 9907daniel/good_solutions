# 09:43 ~ 10:07 + 10:32 ~
#
# 입출력 : weights 의 길이 = 10만 -> nlogn 까지 가능할듯하다
#
# 해쉬맵을 사용해서 같은 사람이 몇명 있나를 봐야하기도 할듯..? 
# 어떻게 같은 사람을 중복 check 하지..? 
#
from collections import Counter

#
# 1) 직접 곱한 숫자들은 곱하지 않는다 -> 그래야 겹치는것들을 고려하지 않는다
# 2) 1배수는 자기자신만 확인한다
# 3) 나머지들은 자기가 있는지를 화인한다 곱하기 나누기를 통해 확인한다
#


def solution(weights):
    results = 0
    dic = {}
    
    for a in weights:
        if a in dic:
            weights[a] += 1
        else:
            weights[a] = 1
    
    for a in dic:
        if dic[a] > 1:
            # 본인을 제외한 모든것을 더한다
            results += (dic[a]*(dic[a]-1))/2
        if a*2 in dic:
            results += dic[a]*dic[2*a]
        if a*2/3 in dic:
            results += dic[a]*dic[a*2/3]
        if a*3/4 in dic:
            results += dic[a]*dic[a*3/4]





    # results = 0
#     dic = {}
    
#     for a in weights:
#         if a in dic:
#             dic[a] += 1
#         else:
#             dic[a] = 1
    
#     for a in dic:
#         if dic[a] > 1:
#             print((dic[a]*(dic[a]-1))/2)
#             results += (dic[a]*(dic[a]-1))/2
#         if a*2 in dic:
#             results += dic[a]*dic[2*a]
#         if a*2/3 in dic:
#             results += dic[a]*dic[a*2/3]
#         if a*3/4 in dic:
#             results += dic[a]*dic[a*3/4]
            
    
    
    