# 10:37 ~ 10:50
#
#
# 슬라이딩 윈도우 문제 같다
#

n, k = map(int, input().split())

l = list(map(int, input().split()))

if k == 1:
    print(max(l))
else:
    
    start_sum = sum(l[:k])
    current_max = start_sum
    for a in range(len(l)-k):

        start_sum -= l[a]
        start_sum += l[a+k]

        current_max = max(start_sum, current_max)

    print(current_max)