# 20:55 ~ 21:04
#
# 전형적인 백트래킹 문제 같다

from itertools import combinations


l,c = map(int, input().split())
words = list(map(str, input().split()))
vo = ['a','e','i','o','u']

words.sort()
answers = []
for a in combinations(words, l):
    
    v = 0
    c = 0
    
    for b in range(len(a)):
        if a[b] in vo:
            v += 1
        else:
            c += 1
    
        if v >=1 and c >= 2:
            answers.append("".join(a))
            break

for a in answers:
    print(a)