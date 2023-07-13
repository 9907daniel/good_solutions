#
# 09:10 ~ 09:30
#
# DP 문제
#
#

n,x = map(int, input().split())

dp = 'p'

for a in range(1, n+1):
    dp = 'b' + dp + 'p' + dp + 'b'

l = list(dp)

count = 0
for a in range(x):
    eat = l.pop()
    if eat == 'p':
        count +=1

print(count)