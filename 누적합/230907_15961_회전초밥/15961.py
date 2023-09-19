# 14:07 ~ 
#
# 놓일수 있는 초밥의 개수 : 300만
# 초밥의 실제 개수 : 3000개 (최대 먹을 수 있는 종류 = 3000)
#
# 만약 쿠폰을 사용한다 = count X BUT 연속 count O
# 
# 순환을 해줘야 하기 때문에... 누적합으로 풀 수 있을꺼 같다..? 
# or
# 매게변수 탐색을 통해 ..? NO
# 
#
# 누적합으로 풀어보자!!
# 1) 시작점 start 에서 start+k 만큼 순환을 하고, 이때 set / dic를 통해 관리를 해준다
#
#
# 반례 1)
# - 만약 a+k 가 len()를 넘는다면


n, d, k, c = map(int, input().split())

sushi = []

for _ in range(n):
    sushi.append(int(input()))
    
dic = {}
dic[c] = 1

current_pallete = []
for a in range(k):
    current_pallete.append(sushi[a])
    if sushi[a] in dic:
        dic[sushi[a]] += 1
    else:
        dic[sushi[a]] = 1

current_max = len(dic)
answer = current_max

for a in range(1,len(sushi)):
    dic[sushi[a-1]] -= 1
    if dic[sushi[a-1]] == 0:
        current_max -= 1

    if a+k-1 < len(sushi):
        if sushi[a+k-1] in dic:
            dic[sushi[a+k-1]] += 1
            if dic[sushi[a+k-1]] == 1:
                current_max += 1
        else:
            dic[sushi[a+k-1]] = 1
            current_max += 1
    else:
        if sushi[a-len(sushi)+k-1] in dic:
            dic[sushi[a-len(sushi)+k-1]] += 1
            if dic[sushi[a-len(sushi)+k-1]] == 1:
                current_max += 1
        else:
           dic[sushi[a-len(sushi)+k-1]] = 1
           current_max += 1
           
    answer = max(answer, current_max)
    
print(answer)

        

