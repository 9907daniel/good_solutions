# 15:07~ 

n = int(input())
l = list(input())


steps = 1e8

count = 0
if 'B' in l:
    count += 1
    
for a in range(len(l)):
    if l[a] == 'R':
        count += 1

steps = min(steps, count)


print(steps)