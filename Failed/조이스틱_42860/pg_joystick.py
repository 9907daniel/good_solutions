
# 핵심은 최소를 찾아 왼쪽 오른쪽 이동 여부가 아니다
# BBBBAAAABA


# 1. 인덱스를 들릴수 있는 모든 순열을 구한다
# 2. 순열을 총해 앞/뒤 이동 거리를 구한다
# 3. 순열에서의 위,아래 또한 구한다

from itertools import permutations

def solution(name):
    new_name = [a for a in name]
    length = [a for a in range(len(new_name))]

    results = []
    for a in permutations(length):
        count = 0
        current = 0
        print(a)
        for b in range(len(a)):
            # 4 3 2 0 3 2 1
            if a[b] != 0:
                if new_name[b] == 'A':
                    continue
                
                if a[b]-current > (len(new_name)-1)-a[b]+1:
                    count += (len(new_name)-1)-a[b]+1
                    # print(0, (len(new_name)-1)-a[current]+1)
                else:
                    count += a[b]-current
                    # print(0, a[b]-current)
                current = b
            
            if ord(new_name[b])-ord("A") > 13:
                count += abs(ord("Z")-ord(new_name[b])+1)
            else:
                count += abs(ord("A")-ord(new_name[b]))
        results.append(count)
        
    # print(results)

name = "JEROEN"   
solution(name)