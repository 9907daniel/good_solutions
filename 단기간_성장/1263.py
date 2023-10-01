# 09:14 ~ 09:51
# 입출력 -> 1000
# 1,000,000 -> N2LogN
# 
#
# 1) 그리디한 접근법을 생각해보자..
# 어떻게 정렬을 하면 매번 최적의 해를 보장할까
#
#
# 3,5 -> 5시에 끝내기 위해 2시에는 시작하자
# 8,14 -> 14시에 끝내기 위해 6시에는 시작하자
# 5,20 -> 20시에 끝내기 위해 최소 15시에는 시작하자 
# 1,16 -> 16시에 끝내기 위해 최소 15시에는 시작하자
#
# 1) 시간차대로 정렬을 하고..
# 2) 작업이 끝나는 시간을 현재 시간으로 두고..
# 3) 다음 작업이 순서가 된다면.. 그만큼 앞당겨 주자..? 
# 4) 다음 업데이트를 다음 작업이 끝나는 시간이 아닌,, 사이에 여유있는 시간까지 고려해보자

n = int(input())
l = []

for _ in range(n):
    l.append(list(map(int, input().split())))

l.sort(key=lambda x:(x[1],x[0]), reverse = True)

# current = l[0][1]
# start_time = l[0][1]-l[0][0]
start_time = l[0][1]

for a in range(1, len(l)):
    # 현재 작업을 최소 끝내야할 시간
    # start_atleast = l[a][1]-l[a][0]
    # 최소 시작해야할 시간이, 전 작업이 끝나는것보다 빠를때
    # tmp = (start_atleast)-current
    if start_time < l[a][1]:
        # 위가 성립한다면.. 중복되기 때문에 일어나는 시간을 앞당기자
        start_time -= l[a][0]
        # 그만큼 앞당겼기 때문에.. 일어나는 시간도 작업이 끝나는 시간이다
        # current = l[a][1]
    else:
        # 중복되지 않거나, 딱 그때 끝난다면 starts는 업데이트 해주지말고..
        # 현재 작업이 끝나는 시간 - 더 일찍 시작해서 끝내는게 가능하다면..
        # current = l[a][1]-tmp
        start_time = l[a][1]-l[a][0]
    
    
    if start_time < 0:
        start_time = -1
        break

if start_time < 0:
    print(-1)
else:
    print(start_time)
    
    
    











