# 09:07~ 09:47
#
# 입력값 : 길이 = 30
# 
# 알고리즘 : 스택 / 큐
#
#
# 예제
# (()[[)])([])
#
# (([])
#
# (()())[[][[][]]]
#       03   3     
#       FFTFFTFTTT
#   (2+2*2) -> 8 
#   TFTF
#
# [[[][]][[[[][]][]]]] 

stack = []
l = list(input())
total = []
current = 0
is_opening = True
tmp = []

## (()[[]])
# (((()))((())))

for a in l:
    # if stack is empty when we pop 
    # we add to total count
    if a == '[' or a =='(':
        stack.append(a)
        is_opening = True
    else:
        if len(stack) == 0:
            total = [0]
            break   
        x = stack.pop()
        if a == ']':
            if x != '[':
                total = [0]
                break
            else:
                if is_opening:    
                    current += 3
                else:
                    current = current*3
                is_opening = False
                if len(stack) == 0:
                    total.append(current)
                    current = 0
        elif a == ')':
            if x != '(':
                total = [0]
                break
            else:
                if is_opening:    
                    current += 2
                else:
                    current = current *2
                is_opening = False
                if len(stack) == 0:
                    total.append(current)
                    current = 0
print(total)
