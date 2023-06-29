# https://www.acmicpc.net/problem/1034
# 10:20 ~ 11:07
# 
# 입출력 50, 50, 1000
#
# 현재 풀이 -> 50*50*50*50....50 (X
#        -> 50*50 -> OK
#
# 행행행행 열
#        열
#
#
# <풀이>
# : 백트래킹(시간초과), 완전탐색(?), 그리디(?
# 
# 행을 고를수 있는 모든 조합을 구하고, 그 값에서 최댓값을 비교하면..?
# -> 1000! 이 되어서 timeout(?)
#
# ->-> 모든 조합을 구할 필요가 없이.. 누른다 / 안누른다 의 조합만 구하면 됟나
# ->->-> 50*50이기 때문에 백트래킹도 가능
#
# 최댓값인 조합을 구하고..> 나머지는 k를 동일하게만 눌르면..?

n,m = map(int, input().split())
graph =[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

k = int(input())

press = [False]*m

if k >= m:
    k = m

# TFTTFTF
# 00101010100101



# 우선 m range 안에 누를수 있는 조합들을 구한다
visited = [False]*m
results = []
tmp = [False]*m
def combinations(start):
    if start == k:
        if tmp not in results:
            results.append(tmp[:])
        return
    
    for a in range(m):
        # 같은 버튼을 두번 누른다
        if start+2 <= k:
            combinations(start+2)
            
        # 한번만 누른다
        if tmp[a]:
            tmp[a] = False
            combinations(start+1)
        else:
            tmp[a] = True
            combinations(start+1)
        tmp[a] = False

combinations(0)
print(results)







