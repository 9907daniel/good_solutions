# 14:10 ~  15:35
# 그냥 빡구 -> 시간초과 생각 우선 하지 말자

# 1) ---- 
def type_1(a,b,graph,n):
    count = -1e8
    
    # 누워있는
    if b+3 < n:
        if b+4 == n: 
            count = sum(graph[a][b:])
        else:
            count = sum(graph[a][b:b+4])
    # 서있는
    if a+3 < n:
        another = 0
        for j in range(4):
            another += graph[a+j][b]
        count = max(count, another)
    return count


def type_2(a,b, graph,n):
    count = -1e8
    
    # 자세 1)
    #  --|
    #    |--
    if b+2 < n and a+1 <n:
        tmp = 0
        for j in range(2):
            tmp += graph[a][b+j]
        for i in range(2):
            tmp += graph[a+1][b+i+1]
        count = tmp
            
    # 자세 2) 
    #    |--
    #  --|    
    if b+2 < n and 0<= a-1:
        tmp = 0
        for j in range(2):
            tmp += graph[a][b+j]
        for i in range(2):
            tmp += graph[a-1][b+i+1]
        count = max(count, tmp)
        
    # 자세 3) 
    #  |
    #  -- 
    #    |    
    if b+1 < n and a+2 < n:
        tmp = 0
        for j in range(2):
            tmp += graph[a+j][b]
        for i in range(2):
            tmp += graph[a+1+i][b+1]
        count = max(count, tmp)        
        
    # 자세 4) 
    #    |
    #  -- 
    # |    
    if 0<= b-1 and a+2 < n:
        tmp = 0
        for j in range(2):
            tmp += graph[a+j][b]
        for i in range(2):
            tmp += graph[a+1+i][b-1]
        count = max(count, tmp)
    return count

def type_3(a,b, graph,n):
    count = -1e8
    
    # 자세 1)
    #  ----|
    #      |
    if b+2 < n and a+1 <n:
        tmp = graph[a+1][b+2]
        for j in range(3):
            tmp += graph[a][b+j]
        count = tmp
            
    # 자세 2) 
    #  |
    #  |----
    if b+2 < n and a+1 <n:
        tmp = graph[a][b]
        for j in range(3):
            tmp += graph[a+1][b+j]
        count = max(count, tmp)
        
        
    # 자세 3) 
    #    |
    #    | 
    #  --|    
    if b+1 < n and 0<=a-2:
        tmp = graph[a][b]
        for j in range(3):
            tmp += graph[a-j][b+1]
        count = max(count, tmp) 
               
        
    # 자세 4) 
    #  |--
    #  | 
    #  |   
    if b+1<n and a+2 < n:
        tmp = graph[a][b+1]
        for j in range(3):
            tmp += graph[a+j][b]
        count = max(count, tmp)  
    return count

def type_4(a,b, graph,n):
    count = -1e8
    
    # 자세 1)
    #    |
    #   ====
    if b+2 < n and a+1 <n:
        tmp = graph[a][b+1]
        for j in range(3):
            tmp += graph[a+1][b+j]
        count = tmp
    # 자세 2) 
    #  ====
    #   |
    if b+2 < n and a+1 <n:
        tmp = graph[a+1][b+1]
        for j in range(3):
            tmp += graph[a][b+j]
        count = max(count, tmp)
         
    # 자세 3) 
    #    |
    #  ==| 
    #    | 
    if b+1 < n and a+2 <n:
        tmp = graph[a+1][b]
        for j in range(3):
            tmp += graph[a+j][b+1]
        count = max(count, tmp)
               
    # 자세 4) 
    #  |
    #  |==
    #  |   
    if b+1<n and a+2 < n:
        tmp = graph[a+1][b+1]
        for j in range(3):
            tmp += graph[a+j][b]
        count = max(count, tmp)  
    return count

def type_5(a,b, graph,n):
    count = -1e8
    # 자세 1)
    #   ㅁㅁ
    #   ㅁㅁ
    if b+1 < n and a+1 <n:
        for i in range(2):
            for j in range(2):
                count += graph[a+i][b+j]
    return count



test_count = 1
results = []

while True:
    n = int(input())
    if n == 0:
        break
    else:
        current_max = -1e8
        graph = []
        for _ in range(n):
            graph.append(list(map(int, input().split())))
    
        for a in range(n):
            for b in range(n):
                current_max = max(current_max, type_1(a,b, graph, n))
                current_max = max(current_max, type_2(a,b, graph, n))
                current_max = max(current_max, type_3(a,b, graph, n))
                current_max = max(current_max, type_4(a,b, graph, n))
                current_max = max(current_max, type_5(a,b, graph, n))
        results.append([test_count, current_max])
        test_count += 1

for a in range(len(results)):
    print(str(results[a][0]) + ". " + str(results[a][1]))