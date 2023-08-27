# 10:10
# 1) 처음에 들어온 값부터 구슬 깨기가 가능할까..?
#
#
# 2) 달팽이 - 1의 단위로 2번씩 회전
#
#
# 3) -1이 아닌것을 전부 배열에 남고 나열한다
#

n,m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))
    
orders = []

for _ in range(m):
    orders.append(list(map(int, input().split())))

start_x = (n//2)
start_y = (n//2)

dx = [0,1,0,-1]
dy = [-1,0,1,0]

one = 0
two = 0
three = 0

def magic(graph, attack):
    if attack[0] == 1:
        for a in range(1, attack[1]+1):
            if start_x-a >= 0:
                graph[start_x-a][start_y] = -1
    if attack[0] == 2:
        for a in range(1, attack[1]+1):
            if start_x+a < n:
                graph[start_x+a][start_y] = -1
    if attack[0] == 3:
        for a in range(1, attack[1]+1):
            if start_y-a >= 0:
                graph[start_x][start_y-a] = -1
    if attack[0] == 4:
        for a in range(1, attack[1]+1):
            if start_y+a < n:
                graph[start_x][start_y+a] = -1
    return graph


linear =[]
def move_marvels(depth, depth_count, x, y,direction):    
    global linear
    if x <= 0 and y <= 0:
        return
    
    for a in range(depth):
        nx = dx[direction]+x
        ny = dy[direction]+y
        
        if graph[nx][ny] != -1 and graph[nx][ny] != 0:
            linear.append(graph[nx][ny])    
        x,y = nx,ny
        
        if x ==0 and y == 0:
            return
    
    if 0<= direction < 3:
        direction += 1
    elif direction == 3:
        direction = 0
        
    if depth_count == 1:
        move_marvels(depth+1,0, x,y, direction)
    else:
        move_marvels(depth, depth_count+1,x,y,direction)

def kill_marbles(linear):
    global one
    global two
    global three
    print("start")
    print(linear)
    current = -10
    current_stack = []
    popped = False
    for a in range(len(linear)-1,-1,-1):
        if linear[a] != current:
            if len(current_stack) >= 4:
                for b in range(len(current_stack)):
                    if linear[current_stack[b]] == 1:
                        one += 1
                    elif linear[current_stack[b]] == 2:
                        two += 1
                    elif linear[current_stack[b]] == 3:
                        three += 1
                    
                    linear.pop(current_stack[b])
                    popped = True
            current = linear[a]
            current_stack = [a]
        else:
            current_stack.append(a)
            # 터트리지 않아도 괜찮아도 마지막으로 왔다면 터트림 확인해주기
            if a == 0 and len(current_stack) >= 4:
                for b in range(len(current_stack)):
                    if linear[current_stack[b]] == 1:
                        one += 1
                    elif linear[current_stack[b]] == 2:
                        two += 1
                    elif linear[current_stack[b]] == 3:
                        three += 1
                    linear.pop(current_stack[b])
    print(linear)
    return linear, popped
        
def change_graph(linear):
    new = []
    # current = -100
    current_stack = []
    count = 0
    max_limit = (n*n)-2

    if len(linear) > 0:
        current = linear[0]
        current_stack.append(linear[0])
    else:
        return new
    # print(linear)
    for a in range(1,len(linear)):
        if linear[a] != current:
            new.append(len(current_stack))
            new.append(current)
            count += 2
            if count > max_limit:
                return new
            
            current_stack = []
            current = linear[a]
            current_stack = [linear[a]]
            
            if a == len(linear)-1:
                new.append(len(current_stack))
                new.append(current)
                count +=2
                if count > max_limit:
                    return new
                break
        else:
            current_stack.append(linear[a])
            # 반례
            if a == len(linear)-1:
                new.append(len(current_stack))
                new.append(current)
                count +=2
                if count > max_limit:
                    return new
                break
    return new

def change_marvels(depth, depth_count, x, y,direction, linear, linear_order):    
    if x <= 0 and y <= 0:
        return graph
    
    for a in range(depth):
        nx = dx[direction]+x
        ny = dy[direction]+y
        
        if linear_order < len(linear):
            graph[nx][ny] = linear[linear_order]
        else:
            graph[nx][ny] = 0
        linear_order += 1
        x,y = nx,ny
        
        # if x ==0 and y == 0:
        #     return
    
    if direction < 3:
        direction += 1
    elif direction == 3:
        direction = 0
        
    if depth_count == 1:
        return change_marvels(depth+1,0, x,y, direction, linear, linear_order )
    else:
        return change_marvels(depth, depth_count+1,x,y,direction, linear, linear_order)



    
for a in range(m):
    linear = []
    graph = magic(graph, orders[a])
    move_marvels(1, 0, start_x, start_y, 0)
    while True:
        linear, popped = kill_marbles(linear)
        if popped != True:
            break
            
    linear = change_graph(linear)
    # print(linear)
    
    graph = change_marvels(1, 0, start_x, start_y, 0, linear, 0)
    
answer = one*1 + two*2 + three*3

print(int(answer))

# [1, 2, 1, 1, 2, 2, 1, 1, 1, 3, 1, 2, 2, 3, 2, 1, 2, 3, 1, 1, 1, 3, 2, 2, 1, 3, 2, 2, 1, 3]