# 13:34 ~  13:43
# 
# 
# 
# 
n = int(input())

l = []

for _ in range(n):
    l.append(int(input()))
    
l.sort()

most = 0
for a in range(len(l)):
    consecutive = 1
    # previous = l[a]
    for b in range(a+1, len(l)):
        if l[b] < l[a]+5:
            consecutive += 1
            if b == len(l)-1:
                most = max(most, consecutive)
        else:
            most = max(most, consecutive)
            break

if len(l) == 1:
    print(4)
else:
    if most >= 5:
        print(0)
    else:
        print(5-most)
    
    




