
## 시소짝궁 lv2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/152996

### 알고리즘 사용 : 해쉬맵 / 카운터
- 4번정도 실패 해본 문제 같다..
- 이상하게 풀이가 정말 안떠올른다
- 완탐을하면 당연히 TLE
- 한번의 탐색만 진행해야 하기 때문에 자료구조를 활요한다 -> Counter / 해쉬맵으로 기록을한다
    - 여기서 포인트는 해쉬맵보다는 곱하기를 해주지 말아라는거다..
    - iterate를 할때 확인만 해주자
    - weights 를 iterate 하지말고 dic 을 iterate

### 단계
- 생략

### 코드리뷰
```py

def solution(weights):
    results = 0
    dic = {}
    
    for a in weights:
        if a in dic:
            weights[a] += 1
        else:
            weights[a] = 1
    
    for a in dic:
        if dic[a] > 1:
            # 본인을 제외한 모든것을 더한다
            results += (dic[a]*(dic[a]-1))/2
        if a*2 in dic:
            results += dic[a]*dic[2*a]
        if a*2/3 in dic:
            results += dic[a]*dic[a*2/3]
        if a*3/4 in dic:
            results += dic[a]*dic[a*3/4]
               
```
