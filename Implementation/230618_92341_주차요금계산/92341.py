import math

# 구현문제 같음.
# 2:48 ~ 3:30

def even_calculator(fees, car_num, car_times):
    total = fees[1]
    total_time = 0
    
    for b in range(0,len(car_times)-1, 2):
        total_time += car_times[b+1] - car_times[b]
        
    if total_time < fees[0]:
        return total
    else:
        total += math.ceil(((total_time-fees[0])/fees[2]))*fees[3]
    return total

def odd_calculator(fees,car_num,car_times, last):
    total = fees[1]
    total_time = 0
    for b in range(0, len(car_times)-2, 2):
        total_time += car_times[b+1] - car_times[b]
    
    total_time += last - car_times[-1]

    if total_time < fees[0]:
        return total
    else:
        total += math.ceil((total_time-fees[0])/fees[2])*fees[3]
    return total
    


def solution(fees, records):
    dic = {}
    
    for a in records:
        l = list(a)
        new_l = "".join(l[6:10])
        hour = "".join(l[0:2])        
        minute = "".join(l[3:5])
        joined = int(hour)*60 + int(minute)

        if int(new_l) not in dic:
            dic[int(new_l)] = [int(joined)]
        else:
            dic[int(new_l)].append(int(joined))
        
    last = (23*60)+59
    
    for a in dic:
        if len(dic[a]) == 1:
            if last-dic[a][0] > fees[0]:
                dic[a] = fees[1] + math.ceil((((last-dic[a][0])-fees[0])/fees[2]))*fees[3]
            else:
                dic[a] = fees[1]
            
        elif len(dic[a]) % 2 == 0:
            dic[a] = even_calculator(fees, a, dic[a])
            
        elif len(dic[a]) % 2 == 1:
            dic[a] = odd_calculator(fees, a, dic[a], last)
            
    new_list = dict(sorted(dic.items()))
            
    results = []
    for a in new_list:
        results.append(new_list[a])
        
    return results
    
    
    
    