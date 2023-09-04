# 10:33 ~  11:08
# 
# 합집합을 해주는 Union Find 문제이다
# 
# 

import sys
sys.setrecursionlimit(100000)

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

answers = []
parent = []

for a in range(n+1):
    parent.append(a)

for _ in range(m):
    i,j,k = map(int, input().split())
    if i == 1:
        if parent[j] != j:
            parent[j] = find(j)
        if parent[k] != k:
            parent[k] = find(k)
            
        if parent[j] == parent[k]:
            answers.append("YES")
        else:
            answers.append("NO")
    elif i == 0:
        union(j,k)

for a in answers:
    print(a)



