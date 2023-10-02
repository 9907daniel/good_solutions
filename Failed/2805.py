#
# 09:04 ~
#
# 나무 길이 : 2억 
#
# 문제)
# 20 15 -> 5
# 15 15 -> 0
# 10 15 -> 0
# 17 15 -> 2  --> 7
#
#
# 떡 문제와 동일하다) 
# 만족을하는 최댓값을 구하자..
#
#
# 풀이)
# 1) 매개변수 탐색은 초기값을 설정 잘해야한다 : 0 ~ max(나무 길이)
# 
#
# 1. 중간값 = 10
# 10 5 0 7 -> 27
#
#

n, target = map(int, input().split())

l = list(map(int, input().split()))

start = 0
end = max(l)

answer = -1
while start <= end:
    mid = (start+end)//2
    total = 0
    
    for a in range(len(l)):
        if l[a]-mid > 0:
            total += l[a]-mid
        
    if total < target:
        end = mid -1
    elif total >= target:
        start = mid + 1

print(end)
        
    
