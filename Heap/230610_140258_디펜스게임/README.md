## 디펜스게임 lvl2 pg
https://school.programm230610

!!실패!!

### 알고리즘 사용 : heap

- for문을 한번 이상 사용하기에는 입력 예제가 너무 컸다
- 그리디를 사용하기에는 너무 변수가 많았다
- 백트레킹을 사용 하기에도 너무 변수가 컸다

-> heap풀이를 사용해야했다..
- 힙에서 최대값을 사용하기 때문에 e를 삽입하지 말고 -e를 삽입한다 (힙은 minimum부터 꺼내기 떄문이다)
- 힙을 떠올려야하는 문제중에 좋은 예지이다


### 단계
1. iterate 를 한다
2. 체력을 keeptrack하고 그러는동안 힙에다 넣는다
3. 체력이 넘는다면 무적권이 있는동안에는 사용을 하고 힙에서 뺀다 (체력에서 최대값을 다시 제거한다)
4. 무적권이 없다면 게임 끝.

### 복습
```
import heapq

result = 0
current_health = 0
q = []

for e in enemies:
    current_health += e
    heapq.heappush(q, -e)

    if current_health > k:
        if k == 0:
            break
        biggest = heapq.heapppop(q)
        k -= 1
        current_health += biggest
    answer +=1

```
