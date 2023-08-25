# 00:58 ~ 
#
# 알고리즘 : 400만 입출력 + 여러 단위로 나누느것 + 최소값의 최대값을 구한다에서 매개변수 탐색임을 알 수 있다
#
# 매개변수 탐색이 되는 대상은 최소값의 길이 ex) 15cm 를 이진탐색으로 정해준다
# 
# 
# l = 70
# 10 20 35 55 60
#
# start = 0
# end = max = 70
# mid = 35
#
# 0~35 -> smaller -> 
# mid = 17 
# -> 0 ~ 20 + 20~55 + 60 70 .. X -> smaller
#
#
# mid = 8
# -> 0~10 + 10~20 + 20~35 + -> bigger
# mid = 12 (17, 8)
# -> 0~ 20 + 20~35 + 35~55 +55 -> bigger
# 
# 번례)
#
# 1 1 1000
# 800
# 1
# 800
#


n,m,l = map(int, input().split())

checkpoints = []

for _ in range(m):
    checkpoints.append(int(input()))

cuts = []

for _ in range(n):
    cuts.append(int(input()))
checkpoints.append(l)

results = []
for a in range(len(cuts)):
    q = cuts[a]

    current_answer = 0
    start = 1
    end = l
    
    while start <= end:
        # 35에서 시작
        mid = (start+end)//2
        
        count, tmp = 0,0
        for a in range(len(checkpoints)):
            # 0~10, 10~20 ...
            if checkpoints[a]-tmp >= mid:
                count += 1
                tmp = checkpoints[a]
        

        if count > q:
            # if l-tmp < mid:
            #     current_answer = max(current_answer, l-tmp)
            # else:
            start = mid + 1
            current_answer = max(current_answer, mid)
        else:
            end = mid - 1
    print(current_answer)
#     results.append(current_answer)

# for a in results:
#     print(a)
                







