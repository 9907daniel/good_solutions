# 19:50 ~ 20:28
# 
# T = 1000
# 
# 문제는 즉, 접은 길이가 완전히 두깨는 2배, 길이느는 1/2배 인지를 묻는다
# 
# 덥혀 있기 위해서는 0이 1보다 많아야하나..?
#
# 스택을 사용해.. 만약 붙어있는거를 터트린다면..?
#
# 접히는것이기 때문에 무조건 야끝이 달라야한다..?

t = int(input())
answers = []
for _ in range(t):
    l = list(input())
    
    if len(l)%2 == 0:
        answers.append('NO')
        continue
    
    if len(l) == 1:
        answers.append('YES')
        continue
    
    start = 0
    end = len(l)-1
    count = 0
    while start <= end:
        if l[start] != l[end]:
            start += 1
            end -= 1
            count += 1
        else:        
            break
    if count == len(l)//2:
        answers.append('YES')
    else:
        answers.append('NO')
        
for a in answers:
    print(a)
    
    
########################################
## 풀이 2)
answers = []
for _ in range(t):
    l = list(input())
    
    count = 0
    start = 0
    while start < len(l):
        if start == len(l)-1:
            break
        
        if l[start] != l[start+1]:
            start += 1
            count += 1
        start += 1
    
    if len(l)//2 == count:
        answers.append('YES')
    else:
        answers.append('NO')

for a in answers:
    print(a)


############################################################
#### 풀이 1)
t = int(input())

answers = []
for _ in range(t):
    zero = 0
    one = 0

    l = list(input())
    
    if len(l) == 1:
        answers.append('YES')
        continue

    for a in range(len(l)):
        if l[a] == '0':
            zero += 1
        else:
            one += 1
                   
    if zero == one+1 or one == zero+1:
        answers.append('YES')
    else:
        answers.append('NO')

for a in answers:
    print(a)



