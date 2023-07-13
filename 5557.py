# 09:30~ 09:55 + 10:23 ~ 10:33
#
#
# 입출력 : 100
# 백트래킹 / DP / DFS
#
# 풀이 1) - 백트래킹
# 어차피 음수 / 양수 전체 합이기 떄문에 어떤 수를 뭔가 비교하든 상관 없는거 같다
# 역시 시간초과
#
#
# DP 떠올리기 -> 출력값이 2^63까지 가능하니.. 완탐은 안되고..
#
#
###################################
##################################
##################################

n = int(input())

l = list(map(int,input().split()))

l.sort(reverse=True)
# [8 8 8 8 7 4 4 3 2 0]

# dp = [0 for _ in range(n+1)]
# iterate 하면서 뒤에꺼 -,+ 인지 여부를 판단하며 현재 total count 값을 넘겨줌
# for a in range(1, n+1):


def dfs(start):
    
    
    
    
    
    








##################################
##################################
##################################

visited = [False]*n

count = 0
tmp = 0


def combinations(start, calculate):
    global tmp
    global count
    
    # 만약 마지막까지 연산을 했고, 결과가 0<=tmp<=20이라면
    if start == n and tmp >= 0 and tmp <=20:
        print(tmp, )
        count += 1
        return
    
    # 모든거를 전부 iterate
    for a in range(n):
        # 방문처리 안되어있다면
        if visited[a] != True:
            # 방문처리 해줌
            visited[a] = True
            
            # 연산 +를 한다
            if calculate == True:            
                tmp += l[a]
                combinations(start+1, False)
                tmp -= l[a]
            # 연산 -를 한다
            elif calculate == False:
                tmp -= l[a]
                combinations(start+1, True)
                tmp += l[a]
            visited[a] = False
            
combinations(0, True)

print(count)


