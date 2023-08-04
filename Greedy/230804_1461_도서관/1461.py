# 13:40 ~
# 
# 입력 : 50, 10000
# 
# 그리디 + 정렬
# 
# 1. 일단 정렬을 해본다
# 2. m 단위로 끊어서 왔다 갔다 한다
# 3. 하지만 만약 <- -> 가는게 더 효율적이라면 ..?
#
#
#
# -39 -37 -29 -28 -6 0 2 11 
# 
# 반례)
# 가장 큰 숫자는 가기만 하는게 더 좋지 않나..? 
#
# 22 + 56 + 74 + 39 = 65 +
# 
# 39 
# 54 + 16 + 22 -> 131
#
# 우선 모든 조합을 짤라서 구하고..? 여기서 제일 큰값을 제외하고는 제곱을 해준다
# 앞에서 시작 + 뒤에서 시작 둘다 고려해준다..?
#
#
# 입력값을 통해 알 수 있는게 뭘까.. 왜 50.. -> 10,000..?
#

n,m = map(int, input().split())

l = list(map(int, input().split()))

l.sort()

tmp1 = []
tmp2 = []

current = 0
while current < len(l):
    if l[current] < 0:
        tmp1.append(abs(l[current])) 
    else:
        tmp2.append(l[current]) 
    current += 1

tmp2.sort(reverse=True)

total = []
for a in range(0,len(tmp1),m):
    total.append(tmp1[a])

for a in range(0,len(tmp2),m):
    total.append(tmp2[a])

total.sort()
results = 0
for a in range(len(total)-1):
    results += 2*total[a]
results += total[-1]

print(results)
    