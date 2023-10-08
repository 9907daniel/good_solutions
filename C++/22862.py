# 10:55 ~ 
#
# N = 100만 -> NlogN / N 까지만 가능하다
#
# 투포인터를 정하고, 짝수, 홀수를 따로 관리한다.
# 즉, 홀수가 coun가 k 를 넘는자면 멈춘다. 
#
# 양끝 홀수가 반례 같지만.. 어차피 sliding window 로 탐색한다면 다른 케이스까지 고려된다
#
# 반례) 모든게 다 이미 짝수라면


n,k = map(int, input().split())

l = list(map(int, input().split()))

odd = 0
total = 0

answer = 0
right = 0

for a in range(len(l)):
    if l[a] % 2 == 0:
        total += 1            
    else:
        if odd+1 > k:
            answer = max(answer, total)
            right = a
            break
        else:
            odd += 1
            
    if odd < k:
        answer = max(answer, (a-odd+1))
            
for left in range(len(l)-right):

    if l[left] % 2 ==0:
        total -= 1
    else:
        odd -= 1
    
    while right < len(l):
        if l[right]%2 == 0:
            total += 1
        else:
            if odd+1 > k:
                answer = max(answer, total)
                break
            else:
                odd += 1
        right += 1
    
    if odd < k:
        answer = max(answer, (right-left-odd))
    
print(answer)
        