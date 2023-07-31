# 11:22 ~ 11:51
#
# n = 100,000
# -> 그래도 n^2 는 가능하지 않을까
#
# 풀이 1)
# - 기준점을 구하고...
# - 이 기준점을 기준으로 split하는거는 어떨까
#
# 반례) 
# 1 10000 1 1 1 1 90
# 
#
# 9 9 4 1 4 9 9
# 
# 9 18 22 23 24 33 42
# 42 33 24 23 22 18 9
#
# 현재 기준점으로 Sum 최산화
# 23일때
# 23 - 22 - 9
# 33 - 
#
#



n = int(input())

l = list(map(int,input().split()))

summed_honey = l[:]
for a in range(1, len(l)):
    summed_honey[a] = l[a]+summed_honey[a-1]

tmp = []
# 꿀통이 맨 뒤에 있다
start = summed_honey[-1]
for a in range(n-1):
    rn = start-summed_honey[a]-l[a]
    tmp.append()
        
        
        
        
        
        
        
        
    
elif a == len(l)-1:
    
else:
    left, right = l.split(a)