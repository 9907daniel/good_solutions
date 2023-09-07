# 20:38 ~ 20:55 + 21;34
# 
# 입출력 : 용액의 수 = 10만 -> logn, nlogn까지 가능하다
# 
# -99 -2 -1 4 98
# 
# 목표 : 합을 했을때 가장 0에 가까운 숫자
# 
# 즉, 음수라면 차이가 나랑 가장 큰 숫자
#    양수라면 차이가 ...
#
#
# 0에 가장 가꾸운 음수,양수
# max,min을 4개 구하고
# 한번 iterate
# = 100,000*4
#
#
# -99 -2 -1 4 98
#
# current = -1
# 
#
#


n = int(input())
l = list(map(int, input().split()))

l.sort()

start = 0
end = len(l)-1
turn = True

current = abs(l[start] + l[end])
tmp = [l[start],l[end]]
while start < end:
    if abs(l[start]+l[end]) < current:
        tmp = [l[start],l[end]]
        current = abs(l[start]+l[end])

    if l[start]+l[end] < 0:
        start += 1
    else:
        end -= 1

print(*tmp)
        
        
        
        
        







# n = int(input())
# l = list(map(int, input().split()))

# biggest = max(l)
# smallest = min(l)
# closest_negative = min(l)
# closest_positive = max(l)


# for a in range(len(l)):
#     if l[a] >= 0 and l[a] < closest_positive:
#         closest_positive = l[a]
#     elif l[a] < 0 and l[a] > closest_negative:
#         closest_negative = l[a]

# answer = 1e10
# tmp = [1e10,1e10]
# for a in range(len(l)):
#     x = abs(l[a]+biggest)
#     if x < answer:
#         answer = x
#         tmp = [l[a], biggest]
#     x = abs(l[a]+smallest)
#     if x < answer:
#         answer = x
#         tmp = [l[a], smallest]
#     x = abs(l[a]+closest_negative)
#     if x < answer:
#         answer = x
#         tmp = [l[a], closest_negative]
#     x = abs(l[a]+closest_positive)
#     if x < answer:
#         answer = x
#         tmp = [l[a], closest_positive]

# tmp.sort()
# print(*tmp)

    
    
    
    
    





