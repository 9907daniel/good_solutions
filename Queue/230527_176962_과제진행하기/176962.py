from collections import deque

def solution(plans):
    for a in range(len(plans)):
        plans[a][1] = int(plans[a][1][0:2])*60 + int(plans[a][1][3:])
        plans[a][2] = int(plans[a][2])
        
    # 정렬
    plans.sort(key = lambda x : x[1])
    
    current_time = plans[0][1]
    results = []
    q = deque()
    for a in range(len(plans)):
        # 현재 시간이 다음 과제 도달 전이라면 큐 마지막을 실행한다
        # while not next time
            # 만약 과제를 끝낸다면 큐에서 제거를 하고 다음 과제~
        while current_time < plans[a][1] and len(q) > 0:
            if current_time + q[0][2] > plans[a][1]:
                q[0][2] = q[0][2] - (plans[a][1] - current_time)
                break
            else: 
                results.append(q[0][0])
                current_time = current_time + q[0][2]
                q.popleft()
    
        # 1. 현재 시간 + 현재 과제가 다음 과제에 도달하기 전에 끝낸다
        if a != len(plans)-1:
            if plans[a][1] + plans[a][2] <= plans[a+1][1]:
                results.append(plans[a][0])
                current_time = plans[a][1] + plans[a][2]

            # 2. 끝내지 못한다면 큐에 넣는다                
            elif plans[a][1] + plans[a][2] > plans[a+1][1]:
                plans[a][2] = plans[a][2] - (plans[a+1][1]-plans[a][1])
                q.appendleft(plans[a])
                current_time = plans[a+1][1]
        else:
            results.append(plans[a][0])
    
    if len(q) != 0:
        for a in range(len(q)):
            results.append(q[a][0])
    
    
    return results




