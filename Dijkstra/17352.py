
def find(x):
    # 루트 노드가 아니라면 재귀적으로 호출
    if parent[x] != x:
        return find(parent[x])
    return x

def union(a,b):
    a = find(a)
    b = find(b)
    # 더 작은 값으로 합핀다
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
l = []
parent = [0]*(n+1)

# 모든 노드들 본인 자신으로 초기화를 했다..
for a in range(1, n+1):
    parent[a] = a

for a in range(n-2):
    # 연결 되어 있는 두개의 섬
    a, b = map(int, input().split())
    # 연결 되어 있는 섬들을 연결
    union(a,b)

answer = []
for a  in range(1, len(parent)):
    if parent[a] == a:
        answer.append(a)

print(*answer)