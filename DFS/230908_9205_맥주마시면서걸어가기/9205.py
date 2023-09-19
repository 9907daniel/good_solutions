# 16:20 ~ 17:03
# 
# t = 50
# n = 100 (편의점 개수)
# 집, 편의점, 페스티벌 좌표
# 
# <문제 풀이법> 
# 1) 현재 시점에서, x,y를 통한 거리를 구했을때, 만약 50*20 즉 1000미터 미만이면 다음 지점까지 가능
#
#
# <문제 설계>
# 1) for문을 통해 현대 - 다음 좌표. 가능하다면 continue -> else -> fail
# => 50*20
#
# <반례>
# 1) 정렬을 해줘야한다..? -> start_x를 기준으로
# 2) 모든 편의점을 가지 않아도 지나가는중 락 페스트벌이 있다면 GOOD
# 아! DFS / BFS
    

def dfs(visited, familymart, target_x, target_y, current_x, current_y, possible):
    # print(target_x, target_y, current_x, current_y)
    # print(abs(target_x-current_x) + abs(target_y-current_y))
    if abs(target_x-current_x) + abs(target_y-current_y) <= 1000:
        possible = True
        return possible
    
    for a in range(len(familymart)):
        if visited[a] != True:
            if abs(familymart[a][0]-current_x) + abs(familymart[a][1]-current_y) <= 1000:
                visited[a] = True
                x = dfs(visited, familymart, target_x, target_y, familymart[a][0], familymart[a][1], possible)
                if x:
                    possible = True
    return possible

    
t = int(input())

results = []
for _ in range(t):
    n = int(input())
    start_x, start_y = map(int, input().split())
    
    familymart = []
    for _ in range(n):
        familymart.append(list(map(int, input().split())))
    
    festival_x, festival_y = map(int, input().split())
    
    if abs(festival_x-start_x) + abs(festival_y-start_y) <= 1000:
        results.append("happy")
        continue
    possible = False
    visited = [False]*n
    if dfs(visited, familymart, festival_x, festival_y, start_x, start_y, possible):
        results.append("happy")
    else:
        results.append("sad")

    
for a in results:
    print(a)   
    

    
    
    # for a in range(len(familymart)):
    #     current_distance = abs(familymart[a][0]-start_x) + abs(familymart[a][1]-start_y)

    #     if current_distance <= 1000:
    #         pass
    #     else:
    #         possible = False
    #         break
    #     start_x = familymart[a][0]
    #     start_y = familymart[a][1]
    
    
    # if possible:
    #     if abs(festival_x-start_x) + abs(festival_y-start_y) <= 1000:
    #         results.append("happy")
    #     else:
    #         results.append("sad")
    # else:
    #     results.append("sad")