## 이것이 코딩테스트다

### 알고리즘 사용 : 그리디 + 정렬
- 다이익스트라 알고리즘을 익히기 위해 책에 나오는 문제로 여러번 풀어봤다
- 이해하려하고, 변수 이름들을 논리적으로 지어서 더 잘 이해 할 수 있었던거 같다

### 복습

```
import heapq

graph = [[] for _ in range(n+1)]
distance = [1e8]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    # 양쪽 방향이면 graph[b]도 추가

def dijikstra(start):
    q = []
    heapq.heappush(q, (start, 0)) # 시작지점은 항상 0
    distance[start] = 0

    while q:
        current_node, current_distance = heapq.heappop(q)

        if distnace[current_node] < current_node:
            continue
        
        for a in graph[curret_node]:
            sum_distance = a[1] + current_distance
            if sum_distance < distance[a[0]]:
                heapq.heappush(q, (a[0], sum_distance))
                distnace[a[0]] = sum_distance



```