# 12:17 ~
# 입력 : 7*
# 소수인 조건은.. 3, 2 로 나웠을때 둘다 못나누는것..? 

from itertools import permutations

def prime(x):
    for a in range(2, x):
        if x%a == 0:
            return False
    return True
    

def solution(numbers):
    l = [a for a in numbers]
    combi = []
    count = 0
    
    for a in range(1, len(l)+1):
        for b in permutations(l, a):
            x = "".join(b)
            if int(x) not in combi and int(x) != 1 and int(x) != 0:
                combi.append(int(x))
    
    for a in combi:
        if prime(a):
            count += 1

    return count
        