# 09:08 ~ 10:06 + 10:35 ~ 11:06
#
# 구현 문제
#
# 완탐을 하는 대신에.. 일치값을 찾는거는 어떨까..?
# 비어있는 패턴을 찾고..이 패턴이 key에 모든 회전 값에 있다면 ..
# -> 순차적 설명서..? 
# 1,3 -> 3,4 -? 2,6 -> .....
#
#
# 1) 열쇠의 돌이는 전부 고려하지 않아도 괜찮지만 자물쇠의 빈칸은 전부 고려해야한다
# 2) 완탐을 할필요는 없다
# 3) 반례 : 돌기들은 키값고 들어맞지만 같은 영역에 열쇠 돌기가 더 있다..
# 4) 반례 : lock이 1전부 1이면 키에 상관없이 무조건 열린다
#

def rotate_90(graph):
    change = [[0]*len(graph[0]) for _ in range(len(graph))]
    for a in range(len(graph[0])):
        for b in range(len(graph)):
            change[a][len(graph)-b-1] = graph[b][a]
    return change
            
    
def solution(key, lock):

    
    instructions = []
    stone_instrucvtions = []
    # 기준점을 0,0이 아닌 첫번째 발견값으로 잡을까?
    start_x = 0
    start_y = 0
    for a in range(len(lock)):
        for b in range(len(lock)):
            if lock[a][b] ==0:
                if len(instructions) == 0:
                    start_x = a
                    start_y = b
                    instructions.append([0,0])
                else:
                    instructions.append([a-start_x, b-start_y])
    
    print(instructions)
    # 현재 지점이 벽에서는 얼마나 벗어났는지도 추가하자 (중앙값 느낌으로)
    for a in range(len(lock)):
        for b in range(len(lock)):
            if lock[a][b] ==1:
                stone_instrucvtions.append([a-start_x, b-start_y])
    print(stone_instrucvtions) 

    for _ in range(4):
        for a in range(len(key)):
            for b in range(len(key[0])):
                if key[a][b] == 1:
                    stone = True
                    for d in stone_instrucvtions:
                        if 0<=a+d[0]<len(key) and 0<=b+d[1]<len(key[0]):    
                            if key[a+d[0]][b+d[1]] == 1:
                                stone = False
                
                    count = 0
                    for c in instructions:
                        if 0<=a+c[0]<len(key) and 0<=b+c[1]<len(key[0]):    
                            # print(key[a+c[0]][b+c[1]])
                            if key[a+c[0]][b+c[1]] == 1:
                                count += 1
                            else:
                                break
                        # print(key,a,b, count)
                        # print(a+c[0],b+c[1])
                        
                        if count == len(instructions) and stone:
                            return True
        key = rotate_90(key)

    lock_count = 0
    key_count = 0
    for a in range(len(lock)):
        for b in range(len(lock)):    
            if lock[a][b] == 1:
                lock_count += 1
    for a in range(len(key)):
        for b in range(len(key)):    
            if key[a][b] == 0:
                key_count += 1
     
    if lock_count == len(lock)*len(lock):
        return True
    if lock_count == 0 and key_count == 0:
        return False
        

    return False

        
        

    
