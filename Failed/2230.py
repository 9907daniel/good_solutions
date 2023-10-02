# 13:12 ~ 13:39
#
# 입출력 : 100,000
# nlogn
#
# 매개변수 탐색은 안된다 -> 매번 탐색을 해야함
# 투포인터로 풀꺼 같다..
# 투포인터도 시간 초과 걸릴듯 -> 누적합..?
#
# 누적합 풀이인듯..
#
# 풀이법)
# 1) 일단 정렬을 하자
# 2) 양끝을 비교해준다,
#
#
#
# 특이사항)
# 둘어가는 값이 절댓값이다 -> 음수도 가능
#
# m = 5
# 0 0 0 0 0   0 0 0 0  0  0  0  0  0  0  0  0 
#
#   1  3 4 5 7  10 14 18 20 21 22 24 25 30 40 80 
# 1    2 3 4 6 
# 3          3  7 
# 4             6  10  
# 5               
#
n,m = map(int, input().split())
l = []
for _ in range(n):
    l.append(int(input()))
l.sort()

current_ans = 1e10
end = 0
start = 0

# while start <= end and end < len(l):
#     if abs(l[start]-l[end]) < m:
#         end += 1
#     else:
#         current_ans = min(current_ans, abs(l[start]-l[end]))
#         start += 1
# print(current_ans)

for a in range(len(l)):
    start = a
    while end < len(l):
        if abs(l[start]-l[end]) < m:
            end += 1
        else:
            current_ans = min(current_ans, abs(l[start]-l[end]))
            break
    
print(current_ans)

    