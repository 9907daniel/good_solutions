## 신입사원 실1 백준
https://www.acmicpc.net/problem/1946

### 알고리즘 사용 : 그리디 + 정렬
- 테스트케이스까지 계산을 하면 입력값이 200만이 되서 한번에 다 안된다는거를 알수 있다
- 이때 그리디 등 을 떠올릴때, iterate를 한번만 해야하니, stack, min/max, tmp 등으로 현재값을 저장하는 방법을 찾아야한다


### 단계
1. sort list
2. first min is first place
3. 계속 비교하며 최신화


### 복습
```py
graph.sort(key=lambda x : (x[0],x[1]))
    
# 서류 1등은 무조건 pass~ 
# 시작 면접 꼴등은 서류 1등으로 초기화 시킨다
current_last = graph[0][1]
for a in range(1, len(graph)):
    if graph[a][1] > current_last:
        n -= 1
    current_last = min(current_last, graph[a][1])
results.append(n)
```