# 20:12 ~ 20:53
#
# 단어수 = 20,000
# 알파벳 길이 = 100
# 
# 20,000 * 100 = 2,000,000
# 2만*2만을 할 필요 없이, -> 전체를 그냥 해쉬에 넣어주자..
#
# 반례 1) 길이 0 접두사 처리
# 반례 2) 중복 단어
# 반레 3) 접두사 비교시 맨앞에 단어를 찾자
#
import sys

n = int(input())
l = []
worded = []
dic = {}

# 중복된 단어 예외시키기 (필요한지는 모르겠다)
for _ in range(n):
    x = input()
    if x not in worded:
        l.append(list(x))
        worded.append(x)

# 해쉬맵에 접두사 조합 전~부 추가
for a in range(len(l)):
    tmp = ""
    for b in range(len(l[a])):
        tmp += l[a][b]
        if tmp not in dic:
            dic[tmp] = 1
        else:
            dic[tmp] += 1

the_word = ""
current_answer = 0
if_none = True

for a in dic:
    # 접두사 업데이트 할때, 같은 길이는 무조건 앞에꺼를 사용하기 때문에 >= 이 아난 > 로 지정
    if len(a) > current_answer and dic[a] > 1:
        current_answer = len(a)
        the_word = a
        if_none =False

# 만약 최대 접두사가 "" 0 이면
if if_none:
   print(worded[0])
   print(worded[1])
   sys.exit() 

print(the_word)

# 첫 두개만 찾고 break~
answers = []
for a in range(len(worded)):
    if len(answers) == 2:
        break
    
    # 접두사여야하기 때문에 if the word in worded 로 했을때 반례가 생겼다
    if len(the_word) < len(worded[a]):
        if the_word == worded[a][:len(the_word)]:
            answers.append(worded[a])
    else:
        if the_word == worded[a]:
            answers.append(worded[a])

print(answers[0])
print(answers[1])

# 01:20 ~
#
# 최단거리 : BFS가 더 적합할듯 하다
#




results = []

def bfs(n,m,maps, visited):
    visited[0][0] = False
    q = deque()
    q.append((0,0,1))
    
    while q:
        x,y,count = q.popleft()
        maps[x][y] = count
        for a in range(4):
            nx = dx[a]+x
            ny = dy[a]+y
            
            if 0<=nx<n and 0<=ny<m:
                if visited[nx][ny] != True and maps[nx][ny] != 0:
                    visited[nx][ny] = True
                    q.append((nx,ny, count+1))

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    bfs(n,m,maps, visited)
    
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
    
    
    
    