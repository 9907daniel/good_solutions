#
# 15:24
#
#
# 1억이 주어지고 범위 안에서.. -> 이진탐색법
#
#
# n = 10만 -> 이진탐색으로 범쉬에 있는 것들을 빠르게 추려서 +1을 할수도 있다 
#
# 1) 정렬부터 하자
# 2) iterate
#
#
#
# [1, 10], [2, 15], [3, 30], [4, 8], [20, 60]
# 1 3 10 20 30
#
# 1+10 -> 11//2 -> 5



n,m = map(int, input().split())

l = list(map(int, input().split()))

l.sort()

g = []

for _ in range(m):
    g.append(list(map(int, input().split())))
    
results = [0]*m

for a in range(len(l)):
    for b in range(len(g)):
        start = g[b][0] 
        end = g[b][1]
        
        
        while start <= end:
            mid = (start + end) //2
            
            if l[a] == mid:
                results[b] += 1
                break
        
            elif l[a] < mid:
                end = mid - 1
            elif l[a] > mid:
                start = mid + 1

for a in results:
    print(a)