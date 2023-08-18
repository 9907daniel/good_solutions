
## 기타 레슨 실1 백준
https://www.acmicpc.net/problem/2343

### 알고리즘 사용 : 매게변수 탐색
- 매게변수 탐색 감을 잡는데 도와준 문제이다
    - chatgpt 설명 굿
- 핵심은 중간 지점을 찾는게 아니라, 가능한 최댓값 /최솟값을 설정해주는데 이분탐색을 사용하자는 것이다!
- 흔히 매게변수 탐색법은 기준을 잡는데 사용되는 매게체룰 첮눈대 사용되고, 아 가준이 가능한지는 for문이 맡는다  
- 그렇기 때문에 시작과 끝을 잡아주는것이 핵심적인 역할을 한다

### 단계
- 생략

### 코드리뷰
```py
start = max(l)
end = sum(l)
result = 1e8

while start <= end:
    # mid = 27 -> 탐색을 했을때, 27을 안넘는동안 더해주고, 넘어가면 다음 디스크
    mid = (start+end)//2
    
    tmp, count = 0,1
    
    for a in range(len(l)):
        if tmp + l[a] <= mid:
            tmp += l[a]
        else:
            tmp = l[a]
            count += 1
            
    if count <= m:
        result = min(mid, result)
        end = mid - 1
    else:
        start = mid + 1
        
print(result)
               
```
