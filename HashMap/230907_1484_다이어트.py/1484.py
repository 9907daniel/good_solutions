#
#
# n = 15 
# x^2 - y^2 = 15
# x^2 = 15 + y^2
#
# 두개의 숫자를 곱했을떄 딱떨어 질 수 있는덧
#
#
# 1 2 3 5 
# 1, 4, 9, 16 25 ....
#
# 1+15 -> 
# if 1+G in dictionary
# answer.append
# 
n = int(input())

dic = {}
square = []
for a in range(1, 1000000):
    dic[a*a] = a
    square.append(a*a)

results = []

for a in range(len(square)):
    if square[a]+ n in dic:
        results.append(dic[square[a]+(n)])

results.sort()

if len(results) != 0:
    for a in results:
       print(a)
else:
    print(-1)