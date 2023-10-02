# 18:34 ~ 19:10
#
# 8 9 10
# 0 0 10
# 
# 0 9 1 -> 8 1 1 -> 0 1 9 -> 
#               -> 
#       -> 9 0 1 -> 9 1 0 -> 
#               -> 
# 8 0 2 -> 8 2 0 -> 
#       -> 0 8 2 ->
#
# 사실 완탐에 가깝지..
# 규칙 : 모든 경우에, 두가지 수가 있다. -> 하나에 옮기기 vs 다른거에 옮기기 
#       if same 조합 already in 기록 -> dfs X


a,b,c = map(int, input().split())

records = []
visited = [] 
def dfs(x,y,z):
    if x == 0 and z not in records:
        records.append(z)
    
    if x != 0:
        tmp = x+y
        if tmp > b:
            first = tmp-b
            if [first,b,z] not in visited:
                visited.append([first,b,z])
                dfs(first, b, z)
        else:
            if [0,tmp,z] not in visited:
                visited.append([0,tmp,z])
                dfs(0, tmp, z)
        tmp = x+z
        if tmp > c:
            first = tmp-c
            if [first,y,c] not in visited:
                visited.append([first,y,c])
                dfs(first,y,c)
        else:
            if [0,y,tmp] not in visited:
                visited.append([0,y,tmp])
                dfs(0, y, tmp)
    if y != 0:
        tmp = x+y
        if tmp > a:
            second = tmp-a
            if [a,second,z] not in visited:
                visited.append([a,second,z])
                dfs(a, second, z)
        else:
            if [tmp,0,z] not in visited:
                visited.append([tmp,0,z])
                dfs(tmp, 0, z)
        tmp = y+z
        if tmp > c:
            second = tmp-c
            if [x,second,c] not in visited:
                visited.append([x,second,c])
                dfs(x,second,c)
        else:
            if [x,0,tmp] not in visited:
                visited.append([x,0,tmp])
                dfs(x, 0, tmp)
    if z != 0:
        tmp = x+z
        if tmp > a:
            third = tmp-a
            if [a,y,third] not in visited:
                visited.append([a,y,third])
                dfs(a, y, third)
        else:
            if [tmp,y,0] not in visited:
                visited.append([tmp,y,0])
                dfs(tmp, y, 0)
        tmp = y+z
        if tmp > b:
            third = tmp-b
            if [x,b,third] not in visited:
                visited.append([x,b,third])
                dfs(x,b,third)
        else:
            if [x,tmp,0] not in visited:
                visited.append([x,tmp,0])
                dfs(x, tmp, 0)    

     
dfs(0,0,c)

# print(visited)        
records.sort()  
print(*records)
      