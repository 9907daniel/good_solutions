# 22:16 ~ 23:00
# 
# 10^9 = 1000000000
# 999,999,999
# 즉 길이의 최대 = 9 -> 완탐 쌉가능
# 
#
# 1) 최대를 구할때 -> 더한값이 홀수가 가장 많이 나오게 3등분
# 2) 최소를 구할떄 -> 더한값이 짝수가 가장 많이 나오게 3등분
# 
#
# 8 20 19 -> 2
# 8 201 9 = 208 
# 208 
# 2 0 8 -> 10
# 10 -> 1
# 1 -> 1
#
#
# 1) 현재에서 모든 경우로 3등분을 해준다
# 2) 3등분한것을 전부 int로 바꿔줘서 더해준다 -> 투포인터를 사용할까..?
#
# 재귀인가..?

minimum = 1e8
maximum = 0

def dfs(current, count):
    global maximum
    global minimum
    odds = 0
    for a in range(len(current)):
        if int(current[a]) % 2 == 1:
            odds += 1
    
    count += odds
    print(current)
    print(count)

    if len(current) == 1:
        minimum = min(minimum, count)
        maximum = max(maximum, count)
        return
    
    elif len(current) == 2:
        for a in range(len(current)):
            tmp = [current[a]]
            dfs(tmp, count)
    
    elif len(current) >= 3:
        start = 1
        end = start+1
        
        while True:
            left = current[:start]
            mid = current[start:end]
            right = current[end:]
                        
            if len(left) != 0 and len(right) != 0 and len(mid) != 0:                                        
                summed = int("".join(left))+int("".join(mid))+int("".join(right))
                new = list(str(summed)) 
                dfs(new, count)    
            
            if end >= len(current)-1:
                start += 1
                end = start + 1
            else:
                end += 1
                
            if start >= len(current)-2:
                break

l = list(input())

dfs(l, 0)
print(maximum, minimum)
