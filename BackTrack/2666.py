# 13:10 ~  14:32
# 
# 입출력 : 20 -> 19*19*...*19 전체를 다하면 완탐은 힘들꺼 같다
#        -> 백트래킹 (?) 
#        -> 그리디 하게 하기에는 양옆의 옮긺을 고려해야한다
#
# 백트래킹을 한다면, 양쪽의 문을 둘다 대입해보면서 확인..? 
#
# _ 0 _ _ 0 _ _
# 
# F T F F T F -> 1
# 4 
# F T F T F F -> 1
# 3
# F T T F F F -> 1
# 1 
# T F T F F F -> 1
# 6
# T F F F F T -> 3
# -> 틀린 풀이

n = int(input())
first,second = map(int, input().split())
num = int(input())
l = []
for _ in range(num):
	# l = 3 1 6 5
    l.append(int(input()))

smallest = 1e8
def combinations(current, left, right, count):
    global smallest 
    
    # 마지막까지 탐색했다면 최소값 비교
    if current == len(l):
        smallest = min(smallest, count)
        return
    
    open = l[current]
    first_door = abs(left-open)
    #                       left = 현재문 (이제 열려 있기 때문에) 
    combinations(current+1, open, right, count + first_door)
    
    second_door = abs(right-open)
    #                       right = 현재문 (이제 열려 있기 때문에)
    combinations(current+1, left, open, count + second_door)
    
combinations(0, first, second, 0)
print(smallest)



