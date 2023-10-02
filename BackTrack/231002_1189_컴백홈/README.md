## 컴백홈 실1 백준
https://www.acmicpc.net/problem/1189

### 알고리즘 사용 : 백드태킹
- 백트래킹과 DFS에서 살짝 개념적인 딜레마가 있었던 문제이다
    - 이런거 생각하면 아직 기본기가 부족한듯 하다..
- 요약 : DFS를 사용하고 visited = False 초기화를 사용하지 않는다면, 모든 경우의 수를 가지 않고 가장 깊이 있는 곳을 한군대만 갈것이다


### 단계
- 생략

### 복습
- 방문 처리
```py
visited[nx][ny] = True
dfs(graph, visited, count+1, nx,ny)
visited[nx][ny] = False
```
 - 모든 경우의 수를 고려할때 방문처리를 다시 제거해주자..