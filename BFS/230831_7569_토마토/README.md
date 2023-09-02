## 토마토 골5 백준
https://www.acmicpc.net/problem/7569

### 알고리즘 사용 : BFS

- 정석같은 3차원 BFS 문제이다.
- dx,dy값에 위 아래를 보지 말고 for 문이 끝나면 봐준다
- 처음부터 0 0 0 이고 토마토가 하나도 없을때를 생각하는게 중요하다!!
    - 반례의 중요성 (없을꺼 같은것도 항상 입력값을 생각하다)

### 단계
- 처음부터 모든 토마토의 값들을 구해주고, 큐에 넣어준다
- 마지막에 Iterate할때 0 이 남아있다면 -1

### 복습
```py
    while q:
        i,j,k,steps = q.popleft()

        for g in range(4):
            nx = dx[g] + j
            ny = dy[g] + k
            
            if 0<=nx<len(graph[0]) and 0<=ny<len(graph[0][0]):
                if graph[i][nx][ny] == 0 and visited[i][nx][ny] != True:
                    graph[i][nx][ny] = 1
                    visited[i][nx][ny] = True
                    q.append((i,nx,ny,steps+1))
                    
        if i+1<len(graph):
            if graph[i+1][j][k] == 0 and visited[i+1][j][k] != True:
                graph[i+1][j][k] = 1
                visited[i+1][j][k] = True
                q.append((i+1,j,k,steps+1))
                
        if 0<= i-1:
            if graph[i-1][j][k] == 0 and visited[i-1][j][k] != True:
                graph[i-1][j][k] = 1
                visited[i-1][j][k] = True
                q.append((i-1,j,k,steps+1))
```

