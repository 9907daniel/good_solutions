
## 디펜스게임 lv2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/142085#

### 알고리즘 사용 : 그리디 + 힙큐
- 힙 문제 중에 정말 좋은 문제라고 생각한다 (사고력 + 개념)


### 단계
i) 힙에다가 숫자들을 순차적으로 넣어준다
ii) iterate 하면서 빼준다
iii) 0이하가 되는순간 무적권을 전에 사용한척, 지나온 값들 중에서 최댓값을 더해준다

### 코드리뷰
```py
h = []
count = 0
for a in range(len(enemy)):
    heappush(h, -enemy[a])
    
    # 반례 > 0 일때..? --> 왜..?
    if n-enemy[a] >= 0:
        n -= enemy[a]
    elif k > 0 and n-enemy[a] <= 0:
        x = -heappop(h)
        n += x
        n -= enemy[a]
        k -= 1
    else:
        break
    count += 1

return count
```
