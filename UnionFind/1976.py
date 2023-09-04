# 11:27
# 
# 1 -> 1-2
# 2 -> 1-2 & 1-3
# 3 -> 2-3 

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
m = int(input())

parent = []
for a in range(n+1):
    parent.append(a)

orders = []
for _ in range(n):
    orders.append(list(map(int, input().split())))

l = list(map(int, input().split()))

for a in range(len(orders)):
    for b in range(len(orders[a])):
        if orders[a][b] == 1:
            union(a+1, b+1)

current = -1
check = True
for a in range(len(l)):
    if a == 0:
        if parent[l[a]] != l[a]:
            parent[l[a]] = find(l[a])
        current = parent[l[a]]
    else:
        if parent[l[a]] != l[a]:
            parent[l[a]] = find(l[a])
        
        if parent[l[a]] != current:
            check = False
            break

if check:
    print("YES")
else:
    print("NO")


