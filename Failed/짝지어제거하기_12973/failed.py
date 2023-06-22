from collections import deque
# 1. 입출력 : 1,000,000
# 2. iterate를 통해 찾는 즉시 제거를 하고, 병합의 과정을 반복 해야한다 (가장 바깥부터 해야할 필요가 있을까..?)
# 3. 그리디 유력, 큐, 브루트 포스 (시간초과)

def solution(s):
    l = [a for a in s]

    start = 0
    # 모든 문자를 iterate (while문)
    while True:
        for a in range(len(l)):
            # 성립이 안된다
            if a == len(l)-a:
                return 0
            
            # 만약 세트가 있다면 제거
            if l[a] == l[a+1]:
                l.pop(a+1)
                l.pop(a)
                break
        if len(l) == 0:
            return 1
        
    
    
    