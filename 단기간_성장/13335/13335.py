# 16:52 ~ 
#
#
#
n, w, l = map(int,input().split())

trucks = list(map(int, input().split()))
d = [0]*w

count = 1
start = 1
d[-1] = trucks[0]
trucks[0] = 0

while True:   
    count += 1

    if n > 1:
        if sum(d[1:])+trucks[start] <= l: 
            for a in range(w):
                if a == w-1:
                    d[a] = trucks[start]
                    trucks[start] = 0
                    if start < len(trucks)-1:
                        start += 1
                else:     
                    d[a] = d[a+1]

        else:
            if sum(d[1:]) == 0:
                for a in range(w):
                    if a == w-1:
                        d[a] = trucks[start]
                        trucks[start] = 0
                        if start < len(trucks)-1:
                            start += 1
                    else:     
                        d[a] = d[a+1]   
            else:    
                for a in range(w):
                    if a == w-1:
                        d[a] = 0
                    else:     
                        d[a] = d[a+1]
        
        if sum(trucks) == 0 and sum(d) == 0:
            break
    else:
        count = w+1
        break

print(count)
    
