## 인사고과 lvl3 pg
https://school.programmers.co.kr/learn/courses/30/lessons/152995#

### 알고리즘 사용 : 정렬 + 그리디
- 굉장히 좋은 정렬 + 그리디 문제였다
- 순차적으로는 풀었는데 마지막 테케에서 TLE 걸렸다..
    -  고수적인 간단 풀이가 필요했다..


### 단계
1. 내리차순, 오름차순 정렬
2. iterate 중 sum을 넘는게 있다면 return -1
3. 아니라면 내 합보다 큰지 보고, 나머지 점수들도 인센티브 후보인지 확인


### 복습
```py
    wonhoe = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    before = 0
    total = sum(wonhoe)

    count = 1
    for score in scores:
        if wonhoe[0] < score[0] and wonhoe[1] < score[1]:
            return -1
        if before <= score[1]:
            
            if total < score[0]+ score[1]:
                count += 1
            before = score[1]
    
    return count

```