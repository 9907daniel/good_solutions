# 20:06 ~  20:45
# 
# 1 2 3 1 2
#   2 3 1 2 3
#     3 1 2 3 6
# 1,2,3,1,2,3,6,7,9,5,6,8,4,6,3 -> 7
# 1 2 3 1 2 3 5 4 3 6 6 6 7 8 7
# N = 1,000,000 -> 최대 NlogN 
#
# 자료구조, 투포인터 와 같은 방법을 활용해야겠다..
# sliding window..?
# -> TLE
#
n, m = map(int, input().split())

l = list(map(int, input().split()))

count = 0
left = 0
right = 1
start = 1

while True:
    left = 0
    right = left+start
    if right == len(l):
        if sum(l) % m == 0:
            count += 1
        break
    
    current_sum = sum(l[left:right])
    
    if current_sum % m == 0:
        count += 1

    while right < len(l):
        current_sum += l[right]
        current_sum -= l[left]
        
        if current_sum % m == 0:
            count += 1
        right += 1
        left += 1
        
    start += 1

print(count)
        


