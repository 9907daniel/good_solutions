## 프렌즈4블록 lvl2 pg
https://school.programmers.co.kr/learn/courses/30/lessons/17679

### 알고리즘 사용 : 빡구현
- 입출력을 보고 문제를 전반적으로 살펴고 빡구현을 해아한다는 거를 안다
- 문제를 진행하며 빡구현 컨디션이 정말 중요하다는것을 느낌.
- 붙어있는 2x2가 연속으로 몇개 존재하는지 생각하는 순간 문제는 정말 복잡해지는듯하다
    - 문제를 더욱 여유를 가지고 간단하게 생각해볼 필요가 있다
    - 어차피 완전탐색을 한번 할꺼니, 완탐을 하면서 독립적인 2x2를 전부 찾으면 되고, 이 2x2는 겹쳐도 크게 상관없을까다

### 단계
0. while True인동안, 즉 제거되는게 있는 동안에는 while을 돌려준다
1. 완탐을 하며 독립적인 2x2를 전부 remove 배열에 없에준자
2. 완탐을 끝내고 전체 remove에 있는 좌표를  '.'로 바꿔준다
3. 이제 중룍을 사용할꺼다           ^
4. 중룍또한 복잡하게 생각할꺼 없이 -> ㅣ 순으로 탐색을 하며 '.' 존재하는 순간부터 전부 q에 추가해준다



### 복습 
- 중력 구현
```py
for a in range(len(board[0])):
    pull_gravity = False
    q = deque()
    index = -1
    for b in range(len(board)-1,-1,-1):
        if board[b][a] == '.':
            pull_gravity = True
            index = max(b, index)
        else:
            if pull_gravity:
                q.append(board[b][a])
    if pull_gravity:
        count = len(q)
        for b in range(index,-1,-1):
            if count != 0:
                x = q.popleft()
                board[b][a] = x
                count -= 1
            else:
                board[b][a] = '.'
```