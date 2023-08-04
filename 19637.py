n,m = map(int, input().split())
l = []

for _ in range(n):
    l.append(list(input().split()))
   
l.sort(key= lambda x:x[1])

answer = []
for _ in range(m):
    target = int(input())
    
    start = 0
    end = len(l)
    
    while True:
        mid = (start+end)//2 
        
        if mid == len(l)-1 and int(l[mid][1]) < target:
            break
        if mid == 0 and int(l[mid][1]) > target:
            break
        
        if int(l[mid][1]) > target and int(l[mid-1][1]) > target:
            end = mid -1
        elif int(l[mid][1]) < target and int(l[mid+1][1]) < target:
            start = mid +1
        else:
            break
    answer.append(l[mid][0])
    
for a in answer:
    print(a)