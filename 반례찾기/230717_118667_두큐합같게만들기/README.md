## 두 큐 합 같게 만들기 lvl2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/118667

### 알고리즘 사용 : 그리디 + 큐
- 지속적으로 맨 앞에 오는 값들을 비교하며 더 큰거에서 뺴주고 작은거에 더해준다
- 문제는 크게 어렵지 않지만 확인을 멈추는 범위를 설정하는게 중요하다
    - 전채 길이 *2 꺼자는 넉넉하게 확인해야한다
    -> 왔다갔다 할수도 있으니
- 처음에 TLE가 나와서 풀이법이 잘못 됬나 했는데 메반 +- 대신에 sum()을 해줘서 TLE가 나왔다
- 지금 생각해보니 전형적인 그리디 풀이법이다
- 반례가 많기 때문에 충분히 생각을 해주고, 가지치기도 충분히 가능하다
    - 반례 잡기 좋은 문제이다

### 단계
- 생략

### 복습
```py
    if total_sum % 2 == 1:
        return -1
    
    if len(q1) == 1 and sum(q1) != sum(q2):
        return -1
    if sum(q1) == sum(q2):
        return 0
    
    while True:
        # 반례 -> len(total)가 아니라 len(total)*2 -> 양방향의 모든 경우의 수
        if count > (len(q1)+len(q2)):
            return -1
        
        if sum_2 > sum_1:
            x = q2.popleft()
            q1.append(x)
            sum_1 += x
            sum_2 -= x
        else:
            x = q1.popleft()
            q2.append(x)
            sum_2 += x
            sum_1 -= x

        count += 1
        if sum_1 == sum_2:
            return count
    
    +
```