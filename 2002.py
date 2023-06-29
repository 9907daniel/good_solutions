# 13:35 ~ 14:08
# 
# 입력 : 1000 -> 2-3개 for문 가능할수도
# 알고리즘 : 투포인터, 스택, 큐
# 
# 설계 : 만약 exit값이 뒤에 있으면 무조건 추월한거냐..? -> 아닌듯 (모든 차들이 서로를 추월)
# 
# 앞부터 시작 vs 뒤부터 시작
# -> enter배열에서 뒤부터 시작하는게 맞는듯
#
#
# enter = [a,b,c,d]
# exit =  [d,a,b,c]

n = int(input())
enter = []
exit = []
for a in range(n):
    tmp = input()
    enter.append(tmp)
   
for a in range(n):
    tmp = input()
    exit.append(tmp)
    
######## 구현 #########

passed = []
for a in range(len(enter)):
    back = enter[a+1:]
    current = enter[a] # 현대 비교하고 있는 차는 current
    
    for b in range(len(exit)):
        # if exit[b] == current and exit[b] not in passed:
        #     passed.append(exit[b])
        #     break
        if exit[b] == current:
            break
        elif exit[b] in back and exit[b] not in passed:
            passed.append(exit[b])

print(count)   

# a-b-c-d-e
# b-e-d-a-c


