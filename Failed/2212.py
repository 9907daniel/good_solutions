# 10:15
#
# 센서 n개, 집중국 k개
# 입력값 : 배열은 최대 100만 크기이다
# 문제 요구사항 : 주어진 센서 위치에 따라 집중극 k개의 위치를 정하자
# 알고리즘 : 100만 입출력을 갖기 때문에 크게 : 그리디, DP, 이진을 생각할 수 있다
# 
# 2
# 1 _ 3 _ _ 6 6 7 _ 9
#   1           1
#   2 + 3 = 5
# 어느 한쪽에 모여있는것과 상관 없이, n/3개를 나눠서 생각하면 편할듯하다
# 
#
# 어디다 설치를 해야지 최속밧일까?
#
#
# 다 iterate 하는것보다.. 두 차이가 가장 작은 enpoint k개를 찾아도..
#
#
# sum = 32 
# average = 5.3xxx
# 
# 10
# 5
# 3 6 7 8 10 12 14 15 18 20
#   1   1   1    1   1 


n = int(input())
k = int(input())
l = list(map(int, input().split()))

l.sort()

distance = []
for a in range(1, n):
    distance.append(l[a]-l[a-1])

print(distance)

distance.sort(reverse=True)

for _ in range(k-1):
    distance.pop(0)

print(distance)


# d = [0]*len(l)
# # 계속 하나 넘어가면서 swap-out

# for a in range(len(l)):
    









