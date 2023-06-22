## 주차요금계산 lvl2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/92341#

### 알고리즘 사용 : 구현 + 해쉬맵
- 빡구현에 가깝기 때문에 시간복잡도는 크게 신경을 안써도 된다
- 여러 function으로 나눠서 풀면 디버깅하기 쉽다
- 해쉬맵을 활용해 변환하는게 핵심이다


### 단계
1. split / join을 하면서 해쉬맵을 생성한다
2. 생성된 해쉬맵에 있는 배열들을 짝수, 홀수, len==1 으로 나눠서 구현한다


### 복습
1. split
```py
a = "Hello My name is Daniel"

splitted_a = a.split()

b = "23:49 is the time"

splitted_b = b.aplit(":")
```


2. Sort Dictionary
```py
dic = {3=[1,2,3], 2 = [3,4,2]}

sorted_dic = dict(sorted(dic.values()))

#2, 3 ....
```


3. Round Up / Round Down
```py
import math

a = 3

round_up = math.ceil(a/2)
round_down = math.floor(a/2)
```