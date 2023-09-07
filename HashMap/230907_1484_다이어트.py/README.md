
## 다이어트 골5 백준
https://www.acmicpc.net/problem/1484

### 알고리즘 사용 : 해쉬맵
- 출제 의도는 투포인터를 사용하는거 였던거 같다
- 입출력을 확인했을때 해쉬맵으로 탐색을해도 괜찮았을꺼 같았다
- 핵심은 value를 key로 저장하는것이 아니라 value*value를 key, value를 키의 value로 저장하는것

### 단계
- 생략

### 코드리뷰
```py
n = int(input())

dic = {}
square = []
for a in range(1, 1000000):
    dic[a*a] = a
    square.append(a*a)

results = []

for a in range(len(square)):
    if square[a]+ n in dic:
        results.append(dic[square[a]+(n)])

results.sort()

if len(results) != 0:
    for a in results:
       print(a)
else:
    print(-1)
```
