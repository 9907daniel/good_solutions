## 메이즈러너
https://www.codetree.ai/training-field/frequent-problems/problems/maze-runner/description?page=3&pageSize=20

### 알고리즘 사용 : 구현
- 역시 그냥 삼성 빡구현 문제이다 ...


### 단계
1. 회전을 할 수 있다면 간단하게 풀리지만 에러가 난다면 큰일이다.. 


### 복습
```
def rotate_clockwise(l, angle= 90):
    arr = list(map(l, zip(*matrix[::-1])))
    return arr

def rotation_anti_clockwise(l, angle=90):
    arr = list(map(l, zip(*matrix)))[::-1]
    return arr

```