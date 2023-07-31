# 09:47~ 11:05
#
# 입력값 = 8
#
# 입력값이 이정도로 작다면..? 백트래킹을 하면 안되나? 모든 조합을 구하기 위해
# 8!*2
import sys 
sys.setrecursionlimit(100000)


n = int(input())

l = []
for _ in range(n):
    l.append(list(map(int, input().split())))
    

broken = [False]*n
broken_count = 0
hitter_broke = False
victim_broke = False

current_min = 0
tmp = []

# start == 선택된 계란
def combinations(start):
    global broken_count
    global current_min
    global hitter_broke
    global victim_broke
    
    if start >= n:
        return
    
    # # 공격 순서가 된 계란이 깨졌다면 ..
    # if broken[start] == True:
    #     return
          
    # 꺨 수 있는 모든 계란을 고려해보자  
    for b in range(n):
        # 하지만 선택된 계란이 깨져있으면 안되고, 공격 계란과 동이해도 안된다
        # print(l, broken, start, b)
        if broken[b] != True and b != start and broken[start] != True:
            # 부디친뒤에 값을 계산하자
        
            hitter = l[start][0]-l[b][1]
            victim_egg = l[b][0]-l[start][1]
            
            l[start][0] = hitter
            l[b][0] = victim_egg
                        
            # 뿌러졌다면 broken 표시
            # 방문처리는 할 필요가 없다 -> 깨진것이 아닌 이상 다시 선택 할 수 있다
            
            # print(l)
            if hitter <= 0:
                broken[start] = True
                broken_count += 1
                hitter_broke = True
            if victim_egg <= 0:
                broken[b] = True
                broken_count += 1
                victim_broke = True

            current_min = max(current_min, broken_count)
            combinations(start+1)
            
            # 부디친 피해를 다시 복구 시키자
            l[start][0] += l[b][1]
            l[b][0] += l[start][1]
            
            # 이번 iteration에 깨졌는지를 확인해야한다
            if hitter_broke:
                broken[start] = False
                broken_count -= 1
                hitter_broke = False
            if victim_broke:
                broken[b] = False
                broken_count -= 1
                victim_broke = False
        else:
            combinations(start+1)
        

combinations(0)
print(current_min)
