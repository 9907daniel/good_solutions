# 11:11 ~ 11:29
# 
# [0,...,0] = l(A) = N 인 배열이 있다
#
# i) 원소 하나를 +1 하거나..
# ii) 배열 전체를 x2 하거나
# 
# 
# 16 16 16
# 1 1 1
# 2 2 2
# 4 4 4
# 8 8 8
# 16 16 16 -> 7
#
#
# 풀이법) 0,0,0 을 특정 배열로 만들려 하지 말고, 
# B 배열을 0,0,0..0 으로 만드려 하자 (반대로 생각하기)
#
#

n = int(input())
b = list(map(int, input().split()))

steps = 0
if sum(b) != 0:
    while True:
        above_zero = 0
        for a in range(len(b)):
            if b[a] !=  0:
                above_zero += 1

        count = 0
        for a in range(len(b)):
            if b[a] % 2 != 0:
                b[a] -= 1
                steps += 1
            elif b[a] != 0:
                count += 1
        if count == above_zero:
            for a in range(len(b)):
                b[a] = b[a]//2
            steps += 1
                
        if sum(b) == 0:
            break
print(steps)
        
            
            
            
            
            
            
            

