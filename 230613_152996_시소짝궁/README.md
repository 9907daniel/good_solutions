# 시소짝궁 lv2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/152996

### 알고리즘 사용 : 헤쉬맵
- 여러번 풀이를 떠얼렸지만 전부 시간초과 (n^2)
- n복잡도로 푸는 방법을 잘 못 떠올렸다
- 해쉬맵을 활용하기 좋은 문제 같다 (해쉬맵을 사용하면 중복 걱정을 안해도 된다)
- *2를 하지말고 /2.. 이런식으로 계속하자


### 단계
1. Count with Hashmap
2. iterate through weights
3. Calculate


### 복습
- 해쉬맵
```
weights = [1,2,3,4,5,5]

for a in weights:
    if a not in dic:
        dic[a] = 1
    else:
        doc[a] += 1

```
