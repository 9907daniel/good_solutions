# 23:55
# 
# 
# 1 100
# 8 5
# 3 5
# 
# 1) 모든 조합들을 구해본다..? 
# 
# 3
# 213 295
# 153 24
# 15 233
# 190
# -1
# 
# 

max_answer = 0

def hit(eggs, start, visited):
    global max_answer
    # print(eggs)
    
    check = 0
    for a in range(len(eggs)):
        if eggs[a][0] < 1:
            check += 1
    
    max_answer = max(max_answer, check)
    
    if check == len(eggs):
        return
    
    if start == len(eggs):
        return
    
    for a in range(len(eggs)):
        if eggs[start][0] > 0:
            if eggs[a][0] > 0 and a != start:
                eggs[a][0] -= eggs[start][1]
                eggs[start][0] -= eggs[a][1]
                hit(eggs,start+1, visited)
                eggs[a][0] += eggs[start][1]
                eggs[start][0] += eggs[a][1]
        else:
            hit(eggs,start+1, visited)

            
n = int(input())
eggs = []

for _ in range(n):
    eggs.append(list(map(int, input().split())))

visited = [False]*len(eggs)

hit(eggs, 0, visited)

print(max_answer)
