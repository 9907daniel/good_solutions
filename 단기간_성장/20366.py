# 23:25~00:00
# 
# N = 600
# H = 1,000,000,000
# 
# 풀이 1) 매게변수 탐색
# 1. 최대를 guess 하는 mid 값 설정
# 2. 가능하다면 answer 기록 후 다른 최솟값 늘려보기
# 3. 안된다면 최솟값 줄이기
# 
# ** 중간지점을 14420 로 잡았다.. 이게 부합하는지 어떻게 찾을까..?  
#   -> 일단 전체 두개의 합이 존재하는 것을 만들면되나..? 그럼 중복값이 생길듯하다..
#
# 2 3 5 5 9 완탐을 한다면.. 600* 599 * 598 * 597
# ... 매게변수 탐색으로 찾을 방법이 없다..
#
# 그렇다면 비슷한 투포인터는 어떻까
#
# 높은 값이 있을때) 이진탐색, 투포인터가 효율적일때가 많다
#

n = int(input())
l = list(map(int, input().split()))
l.sort()

#### 풀이 3) sliding window로 4개 연속을 확인하자
# 이게 최솟값인거를 보장할까?
# 일단 하나의 눈사람에 있는 위 아래는 차이가 최소가 될려면 같이 옆에 붙어 있는거를 하는게 맞나?

answer = 1e13

for a in range(len(l)-3):
    for b in range(a+3, len(l)):
        
        first = a+1
        end = b-1  
        
        current = (l[a]+l[b])-(l[first]+l[end])
        answer = min(answer, abs(current))
        
        if current >= 0:
            first += 1
        else:
            end -= 1
print(answer)
        


# #### 풀이 2)
# # 혹시 언니 동생의 start 격차 가장 적은거를 찾고,
# # 이거를 배열에서 둘다 제거하고
# # 언니 동생 end 격차 가장 적은거를 찾아 두번의 투포인터를 활용한다면..? 

# # 이번 투포인터 문제는 양끝 시작보다 첫,두번째 시작이 맞는듯 -> sliding window
# first = 0
# second = 1

# smallest = 1e10
# record_start = -1
# record_end = -1

# total_difference = 0

# while second < len(l):
#     difference = abs(l[second]-l[first])
    
#     if difference < smallest:
#         smallest = difference
#         record_start = first
#         record_end = second
#     first += 1
#     second += 1

# total_difference += abs(l[record_start]-l[record_end])
# l.pop(record_start)
# l.pop(record_end)

# first = 0
# second = 1

# smallest = 1e10
# record_start = -1
# record_end = -1

# total_difference = 0

# while second < len(l):
#     difference = abs(l[second]-l[first])
    
#     if difference < smallest:
#         smallest = difference
#         record_start = first
#         record_end = second
#     first += 1
#     second += 1

# total_difference += abs(l[record_start]-l[record_end])

# print(total_difference)


#### 풀이 1)
# start = 0
# end = l[-1]

# start2 = 1
# end2 = l[-2]

# difference = 1e12
# while start <= end:
#     # start, end가 하나만 움직이는거는 크게 지장이 없을꺼 같다
#     # 누나, 동생 양끝 중에 같이 움직여야하나..? -> 하나만 움직이면 뭔가 격차가 커지는듯
#     first = abs(l[end]-l[start])    
    
#     while end2 <= start2:
#         second = abs(l[end2]-l[start2])
#         difference(min(difference, abs(first-second)))
#         start
    
    


