

def find(a):
    if parent[a] != a:
        return find(parent[a])
    return a

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


v,e = map(int, input().split())

parent = [0]*(v+1)

for a in range(1, v+1):
    parent[a] = a

for _ in range(e):
    a,b = map(int, input().split())
    
    union(a,b)
    
    if parent[a] != a:
        parent[a] = find(parent[a])
    if parent[b] != b:
        parent[b] = find(parent[b555555555t])