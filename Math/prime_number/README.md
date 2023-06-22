## 소수 개수 찾기 lvl2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/42839

### 알고리즘 사용 : 완전탐색 + Math
- 그냥 소수인지 여부를 찾을 수 있다면 된다


### 단계
- 생략

### 복습
find Prime
```
def prime(x):
    for a in range(2, x):
        if x % a == 0:
            return False

    return True
```
