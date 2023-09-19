# 1-5   X
# 2-6   X
# 7     O
# 8     O
# 7-8   O 
# 9     O 
# 10    X
# 3-10  X
# 4     X
# 
# 

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

n,m = map(int, input().split())

truth = list(map(int, input().split()))

parties = []

for a in range(m):
    parties.append(list(map(int, input().split())))
    

parent = []
for a in range(n+1):
    parent.append(a)

# 일단 전부 연결하고.. 마지막에 for문을 돌며 내가 속한곳에 진실을 아는사람도 있다면.. NOPE


for a in range(len(parties)):
    for b in range(len(parties[a])-2):
        union(parties[a][1],parties[a][b+2])

count = 0
for a in range(len(parties)):
    can_tell = True
    for b in range(len(parties[a])-1):
        
        if parties[a][b+1] != parent[parties[a][b+1]]:
            parent[parties[a][b+1]] = find(parties[a][b+1])
        
        for c in range(len(truth)-1):
            if truth[c+1] != parent[truth[c+1]]:
                parent[truth[c+1]] = find(truth[c+1])
            
            
            if parent[parties[a][b+1]] == parent[truth[c+1]]:
                can_tell = False
    
    if can_tell:
        count += 1

print(count)


