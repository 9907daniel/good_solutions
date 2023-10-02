# 22;54 ~ 
#
# <문제>
# - 모든 빌등 중  가장 많이 보이는것을 구해라
# - 정렬은 하면 안됀다
#
#
# N = 50 이다.. -> 생각보다 작네..?
# 매게변수 탐색을 이용해 보자
#
#
# <설계>
# for a in current
#    ~ for b in current (destination)
#       if tmp >= current:
#          + 1 break
# 
# 


n = int(input())

l = list(map(int, input().split()))

current_max = 0
for a in range(n):
    if a == 0:
        pass
    elif a == n-1:
        pass
    else:
        current = l[a]
        left, right = l[:a], l[a+1:]
        
        for b in range(len(left)-1,-1,-1):
            left_count = 0 
            for c in range(len(left)-1, b-1, -1):
                left_count += 1
                if left[c] >= current:
                    