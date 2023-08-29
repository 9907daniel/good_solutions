# 13:11 ~
# 
# _ _ _ _ _ _ _
# 0 0 0 0 0 0 0 
# 0 0 0 0 0 0 1
# 0 0 0 0 0 0 2
# 
#
# 1 2 3 4 5 6 7 8 9
# 0 0 0 0 0 0 0 1 0 
# 20 21
# 30 31 32
# 40 41 42 43
#
#
from itertools import permutations, combinations
import sys

target = int(input())

possible = [0,1,2,3,4,5,6,7,8,9]
count = 0
for a in range(1,12):
    for b in permutations(range(0,10), a):
        b = list(b)
        b.sort(reverse=True)
        print(b)
        if count == target:

            answer = ""
            for an in b:
                answer += str(an)
            print(answer)
            sys.exit()
        
        if a == 1:
            count += 1
        else:
            for c in range(1,len(b)):
                if b[c] >= b[c-1]:
                    break
                else:
                    if c == len(b)-1:
                        count += 1
        
print(-1)









# descending = []

# def backtrack(target, current, l, count):
#     if count == target:
#         return
    
    
#     pass


# target = int(input())

# l = [0]

# backtrack(target, 0, l, 0)





