# 18:16 ~ 19:03
# 
# 입출력 : 1만이지만 전체 좌표는 100만이다
#  -> 여기서 카메라를 일정 거리마다 설치한다 -> 매게변수 탐색
# 
# target = 떨어져 있는 거리
# 
# 1 _ 3 _5 6 7 _ 9
# 
n = int(input())
k = int(input())
l = list(map(int, input().split()))

l.sort()
start = l[0]
end = l[-1]

while start<=end:
    mid = (start+end)//2
    
    installed = 0
    current = l[0]

    for a in range(1, len(l)):
        if current <= l[a] < current+mid:
            continue
        else:
            installed += 1
            current = current + mid
            if installed > k:
                break
            
    if installed > k:
        start = mid + 1
    else:
        end = mid - 1

print(mid)

#
# 3 _ _ 6 7 8 _ 10 _ 12 _ 14 15 _ _ 18 _ 20
#
#
# 3 6 7 8 10 12 14 15 18 20
# start = 3 mid = 11 end = 20
# start = 
#
# 3 ~ 11
#
#
#
# 1 3 6 6 7 9
# 
# start = 1 mid = 5 end = 9 
# installed = 1, start = 1
# 
#
#
#
    






