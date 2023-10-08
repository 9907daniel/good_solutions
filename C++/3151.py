# 10000 -> N^2logN 
# 
# 10m000m000
# 
#  
# 1) 일단 정렬을 한다
# 
# 
# 


n = int(input())

l = list(map(int, input().split()))

l.sort()

first = 0
second = 1
end = len(l)-1