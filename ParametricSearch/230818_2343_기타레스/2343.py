#
#
#
# 1 2 3 4 5 6 7 8 9
# 최소 -> 최소보다 더 큰 값 찾아지는 T,F 가 스위치 되는 곳을 찾으면 멈춘다
#
# 1 2 3 4 5    6 7    8 9 -> 
#
#
#
n,m = map(int, input().split())

l = list(map(int, input().split()))

# 9, 45 
start = max(l)
end = sum(l)
result = 1e8

while start <= end:
    # mid = 27 -> 탐색을 했을때, 27을 안넘는동안 더해주고, 넘어가면 다음 디스크
    mid = (start+end)//2
    
    tmp, count = 0,1
    
    for a in range(len(l)):
        if tmp + l[a] <= mid:
            tmp += l[a]
        else:
            tmp = l[a]
            count += 1
            
    if count <= m:
        result = min(mid, result)
        end = mid - 1
    else:
        start = mid + 1
        
print(result)