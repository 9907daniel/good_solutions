# 09:05 ~ 09:43
#
# 입출력 : n = 500,000, 각 인덱스 최댓값 = 100만
#
# 알고리즘 : DP, 그리디, 이분탐색 (일부 sort)
# 
# 0 0
# 0 2
# 1 2
# 3 2
# 4 1
# 5 3
# 6 3
#
# 최소로 하면서..?
# 
#
# 이분탐색이라고 생각한다면.. -> max = x,y 중에 최대값
#                       mid = 가능한 step으로 설정
#                       
#                       
# for current -> <=2 를 벗어날대까지
#             -> 나머지는 삭제      -> 그리디적으로
#
#
# 반례)
#  0 0
#  1 1
#  2 0 -> 1 1로 가는게 이득일수도 있는데..? 
#  1 3
#
# 0 0 
# 1 0
# 2 1
#
#
# 풀이 2)
# 임의로 모든 조합들을 만드는거는 가능한가..?
# testing = [[0]*200000 for _ in range(1000000)] -> 메모리 초과
#
# dp
# 0 1 2 3 4 5 6 7 8 9 10
# -----------------------
# 
# 가능한거
# x+1 y  | x y+1 | x+1 y+1 | x+2 y | x y+2 | x+2 y | x+2 y+1 | x+1 y+2 | x+2 y+2
#
# -> 9가지 방법 이 있다..
#
#
# 풀이 3) 
# 반대로 생각해서.. -> 목적지 -> 0까지 가는 최소 회수
#
#
# 12 9
# 0 1
# 1 1
# 2 1
# 2 0
# 1 2
# 3 4
# 3 6 
# 5 8
# 6 1
# 5 10
# 5 7
# 5 9
# 9 9
# 
# 5



# n,t = map(int, input().split())

# l = [[0,0]]

# for _ in range(n):
#     l.append(list(map(int, input().split())))
    
# l.sort(key = lambda x:x[1], reverse = True)
# print(l)
    
#####################################
#####################################
#####################################
#####################################
#####################################

from collections import deque

n,t = map(int, input().split())

l = [[0,0]]

for _ in range(n):
    l.append(list(map(int, input().split())))
    

l.sort(key=lambda x:(x[0],x[1]))

# print(l)
dic = {}
for a in range(len(l)):
    if l[a][0] in dic:
        dic[l[a][0]] = min(a, dic[l[a][0]])
    else:    
        dic[l[a][0]] = a

# x는 항상 y보다 크거나 같을꺼다..?
minimum_answer = 1e8

def bfs(l):
    global minimum_answer
    visited = [False]*len(l)
    
    q = deque()
    q.append((l[0],0, 0))
    visited[0] = True
    
    while q:
        current_tmp, count, current_index = q.popleft()
        
        if current_tmp[1] == t:
            minimum_answer = min(minimum_answer, count)
            continue

        if current_tmp[0]-2 in dic:
            rn = dic[current_tmp[0]-2]
        elif current_tmp[0]-1 in dic:
            rn = dic[current_tmp[0]-1]
        else:
            rn = current_index

        for a in range(rn, len(l)):
            if l[a][0] <= current_tmp[0]+2:
                if l[a][1] <= current_tmp[1]+2 and visited[a] != True:
                    q.append((l[a], count+1, a))
                    visited[a] = True
            else:
                break

bfs(l)
if minimum_answer == 1e8:
    print(-1)
else:
    print(minimum_answer)