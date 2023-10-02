# 15:54 ~ 16:51
# 
# 빡구현 문제이다
# 만약 5000*5000 달팽이를 구현한다면..? 메모리 초과가 날 가능성이 있다
# 
# 
# 
import sys

def snail(length, answer,l):
    # graph[mid][mid] = 1
    current_x = 0
    current_y = 0
    count = 1
    current_length = 1
    current_direction = 'right'

    if l[0]<=current_x<=l[2] and l[1]<=current_x<=l[3]:
        answer[current_x-l[0]][current_x-l[1]] = count

    current_max = 0
    while True:    
        for a in range(2):
            for b in range(current_length):
                count += 1
                if current_direction == 'right':
                    current_y += 1           
                elif current_direction == 'left':
                    current_y -= 1
                elif current_direction == 'up':
                    current_x -= 1
                elif current_direction == 'down':
                    current_x += 1
                    
                
                if l[0]<=current_x<=l[2] and l[1]<=current_y<=l[3]:
                    answer[current_x-l[0]][current_y-l[1]] = count
                    current_max = max(current_max, count)

                if count == length*length:
                    return answer,current_max
                
            if current_direction == 'right':
                current_direction = 'up'
            elif current_direction == 'left':
                current_direction = 'down'
            elif current_direction == 'up':
                current_direction = 'left'
            elif current_direction == 'down':
                current_direction = 'right'  
        current_length += 1 


l = list(map(int, input().split()))

zero_count = 0
for a in range(4):
    if l[a] == 0:
        zero_count += 1
if zero_count == 4:
    print(1)
    sys.exit()

length = (max(abs(l[0]),abs(l[1]),abs(l[2]),abs(l[3]))*2)+1


answer = [[0]*(abs(l[3]-l[1])+1) for _ in range((abs(l[2]-l[0])+1))]

graph, num = snail(length, answer,l)


# graph = [[0]*length for _ in range(length)]
# mid = (length//2)
# [[37, 36, 35, 34, 33, 32, 31], 
#  [38, 17, 16, 15, 14, 13, 30], 
#  [39, 18, 5,  4,  3,  12, 29], 
#  [40, 19, 6,  1,  2,  11, 28], 
#  [41, 20, 7,  8,  9,  10, 27], 
#  [42, 21, 22, 23, 24, 25, 26],
#  [43, 44, 45, 46, 47, 48, 49]]

# for a in graph:
#     print(*a, end = ' ')
    
max_len = len(str(num))

for a in range(l[2]-l[0]+1):
    for b in range(l[3]-l[1]+1):
        print(str(answer[a][b]).rjust(max_len), end= " ")
    print()
# for a in range(4):
#     l[a] = l[a]+mid
#     # 0 0 5 3

# for a in range(l[0], l[2]+1):
#     for b in range(l[1], l[3]+1):
#         answer[a-l[0]][b-l[1]] = graph[a][b]
# for a in answer: 
