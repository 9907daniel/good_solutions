
## 회전초밥 골4 bj
https://www.acmicpc.net/problem/15961

### 알고리즘 사용 : 누적합 + 해쉬맵
- 누적합은 DP의 일부이다!
- 입출력을 보고 완탐은 절대 안된다는것을 판단했다
- 1초에 1억 가능하니 3000만이면 iterate는 가능하다
- 하나 확인하고, 하나 삭제해주고..
- 주위할점은 끝에서가서 index out of bounds 가 뜬다면 다시 처음부터 이어서 추가 해주기

### 단계
- 생략

### 코드리뷰
```py
    if a+k-1 < len(sushi):
        if sushi[a+k-1] in dic:
            dic[sushi[a+k-1]] += 1
            if dic[sushi[a+k-1]] == 1:
                current_max += 1
        else:
            dic[sushi[a+k-1]] = 1
            current_max += 1
    else:
        if sushi[a-len(sushi)+k-1] in dic:
            dic[sushi[a-len(sushi)+k-1]] += 1
            if dic[sushi[a-len(sushi)+k-1]] == 1:
                current_max += 1
        else:
           dic[sushi[a-len(sushi)+k-1]] = 1
           current_max += 1
      
```
