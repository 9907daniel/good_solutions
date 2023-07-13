## 운동 골4 bj
https://www.acmicpc.net/problem/1956

### 알고리즘 사용 : 다익스트라
- 대표적인 다익스트라 / 플로이드와샬 문제다
- 모든 노드의 최소값을 확인한다
- 기존 다익스트라와 다른점은 시작노드를 0으로 초기화하지 않는다는것이다
- 매 노드 확인마다 최소값 비교 확인

### 단계
- 생략 


### 복습
```py
def dijikstra(start):
    global current_max
    q = []
    heappush(q, (start, 0)) # 노드 위치, 거리값
    count = 0
    while q:
        current_node, current_distance = heappop(q)
        
        if count > 0 and start == current_node:
            current_max = min(current_max, distance[start])        
        
        if distance[current_node] < current_distance:
            continue
        
        for a in graph[current_node]:
            summed_distance = current_distance+a[1]
            
            if summed_distance < distance[a[0]]:
                distance[a[0]] = summed_distance
                heappush(q, (a[0], summed_distance))
        count += 1
```