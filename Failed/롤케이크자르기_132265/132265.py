# 12:33 ~
# 입력값 1,000,000 -> 그리디 or stack / deque
#
# 양쪽에서 시작해 중복 되지 않게 담는다. -> 만날 시점에서 서로 개수를 확인한다 
# -> 해쉬맵을 사용해야할듯 싶다..
#

def solution(topping):
    # start = 0
    # end = len(topping)-1
    l = {}
    r = {}
    for a in topping:
        if a in l:
            l[a] += 1
        else:
            l[a] = 1
            
    results = 0
    for a in topping:
        if len(l) == len(r):
            results += 1
        if a in r:
            r[a] += 1
        else:
            r[a] = 1
        l[a] -= 1
    print(results)



    