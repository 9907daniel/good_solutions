# 16:50 ~  
# 
# N = 10만
# 
# 
# 1) 처음에는 끝까지 탐색을 해준다..
# 2) 해서 MAX 인덱스를 찾아주자
# 3) 다시돌아가자
# 
# 

n = int(input())
l = list(map(int, input().split()))

start = 0
end = len(l)-1

answer = 0

while start <= end:
    smaller = min(l[start], l[end])
    difference = end-start-1
    
    answer = max(smaller*difference, answer)
    
    if l[start] < l[end]:
        start += 1
    else:
        end -= 1

print(answer)



# max_index = 0
# current_max = 0

# for a in range(len(l)):
#     if min(l[a],l[0])*(a-1) > current_max:
#         max_index  = a
#         current_max = min(l[a],l[0])*(a-1)
    
# left = 0
# right = max_index

# for a in range(len(l)):
#     left = a
#     current_max = max(current_max, min(l[right],l[left])*(right-left-1))

# print(current_max)
