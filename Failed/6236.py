#
# 09:07 ~ 09:14
#
# 1400 + 400 + 101 -> 1901 / 5 -> 
#
# 100 100 101 300 400 400 500 
#
# 100 400 300 100 500 101 400
#
# 최대값 중 최소값 = 500
# 
# 

n,m = map(int, input().split())

l = []

for _ in range(n):
    l.append(int(input()))
    
initial_max = max(l)

while True:
    start = 0
    end = len(l)


    

