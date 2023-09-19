# 20:47 ~ 
#
# 
# 
# 0-1-3-0
# 3-1-2
# 
# 만약 이어버린 선의 두개 조합이 이미 같은 값을 가지고 있다..? 그러면 끝.
# 아니라면 0
# 

def find(x):
    if parent[x] != x:
        return find(parent[x])
    return x
    
def union(a,b):
    a = find(a)
    b = find(b)

    if a < b :
        parent[b] = a
    else:
        parent[a] = b


n,m = map(int, input().split())
lines = []
for _ in range(m):
    lines.append(list(map(int, input().split())))
        
parent = []

for a in range(n):
    parent.append(a)
    
count = 1
for a in range(m):
    i,j = lines[a][0],lines[a][1]
    
    # 항상 최신화를 시켜주자!!!!!!
    if parent[i] != i:
        parent[i] = find(i)
    if parent[j] != j:
        parent[j] = find(j)
    
    if parent[i] == parent[j]:
        break
    
    union(i,j)
    count += 1



if count > m:
    print(0)
else:
    print(count)



