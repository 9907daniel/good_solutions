

# 풀이
- 단순 풀이는 간단하지만, 입력값이 1,000,000 이기 떄문에 nlogn만 되도 시간초과
- 스택을 사용해야한다


```py
 def solution(s):

    stack = []

    for a in s:
        if len(stack) == 0:
            stack.append(a)
        else:
            if a == stack[-1]:
                stack.pop(-1)
    
    if len(stack) == 0:
        return 1
    else:
        return 0


```