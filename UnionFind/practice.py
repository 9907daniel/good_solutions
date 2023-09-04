
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

# number of nodes, and connections
v,e = map(int, input().split())

# 초기화된 parent list (최상단 부모 현재 내자신)
parent = []
for a in range(v+1):
    parent.append(a)


for _ in range(e):
    i,j = map(int, input().split())
    union(i,j)





















# def find(x):
#     if parent[x] != x:
#         return find(parent[x])
#     return x

# def union(a,b):
#     a = find(a)
#     b = find(b)

#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b

# # 1) 노드의 개수와 간선의 개수를 받는다
# v,e = map(int, input().split())

# # 초기화된 노드 테이블을 만든다
# parent = []
# for a in range(v+1):
#     parent.append(a)
#     # 0,1,2,3....V
    
# for _ in range(e):
#     i,j = map(int, input().split())
#     union(i,j)
    