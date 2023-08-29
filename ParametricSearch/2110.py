# 15:20
#
# 5 3
# 1 2 _ 4 _ _ _ 8 9 10
# 1 _ _ _ _ 1 _ _ _ _
#
# -> 공유기의 크기를 일정하게 크기 잘라서 설치한다
# -> 좌표는 10억까지 가능하다....
#
# -> 매게변수 탐색
#
# 반례
#
# c = 3
# 1 3 4 5 9 10 11 14 19
# 
# mid = 10
# i) 1 3 4 5 9 10 _ 10 11 14 19 -> installed = 2
#
# mid = 5
# 1 2 3 5 _ 5 9 10 _ 10 11 14 19
#
#
#
n,c = map(int, input().split())
l = []

for _ in range(n):
    l.append(int(input()))
l.sort()

start = 0
end = l[-1]

answer = 0

if c == 2:
    print(l[-1]-l[0])
else:
    while start <= end:
        mid = (start+end)//2

        installed, current_starting = 1, l[0]

        for a in range(len(l)):
            if l[a]-current_starting >= mid:       
                installed += 1
                current_starting = l[a]
                
        if installed >= c:
            start = mid + 1
            answer = mid
        elif installed < c:
            end = mid - 1
    print(answer)

# 6 2
# 1 2 _ 4 _ _ _ 8 9 10
# 1 _ _ _ _ _ _ _ _
#
#