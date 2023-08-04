# 09:27 ~ 09:56
#
# 입출력 : 400만 -> 이중 소수만 고려하면 된다.. -> 100만
# 
# 소수 : 2 3 5 7 11 13 17
#
# 알고리즘 : DP를 통해 풀어야할듯..? 혹은 그리디 -> DP 인듯
#
#
# 그냥 DP로 풀면 TLE가 나올듯.. -> 400만을 구해야한다면..? 200만정도까지만 구하면 괜찮지 않을까..
#
# 모든 경우는 구할필요 없고.. 한번의 iteration을 통해서 최소 연속값을 구한다..
# -> 이 연속 값또한 DP 안에 있음 하나의 경우가 될 수 있다
# ex) 11 13 17 -> 11 13 (2 3 5 7)
#
# 풀이 1) DP 실패
#
# 풀이 2) 힌트 - 투포인터
#

n = int(input())

# l = [2,3,5,7]

# for a in range(8, (n+1)//2):
#     if a % 2 != 0 and a % 3 != 0 and a % 5 != 0 and a%7 != 0:
#         l.append(a)

l = []
for a in range(2,):
    if n%a != 0:
        l.append(a)
    
print(l)
# print(len(l)//2)

precount = 0
count = 0
for a in range(len(l)//2+2, 0, -1):
    start = 0
    end = a

    tmp = sum(l[start:end])
    
    for a in range(len(l)-a):
        if tmp == n:
            count +=1
            break
        elif tmp > n:
            break
        tmp -= l[start]
        tmp += l[end]
        start += 1
        end += 1
        precount += 1
# print(precount)

if n <= 8:
    print(count)
elif count == 0 and n not in l:
    print(0)
elif count == 0 and n in l:
    print(1)
else:
    print(count+1)


# dp = [[0]*len(l) for _ in range(len(l))]

# for a in range(len(l)):
#     dp[0][a] = l[a]

# tmp = []
# for a in range(1,len(l)):
#     for b in range(a,len(l)):
#         dp[a][b] = dp[a-1][b]+dp[a-a][b-a]
#         tmp.append(dp[a][b])

# print(tmp)
# print(dp)

