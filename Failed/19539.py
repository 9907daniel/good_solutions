# 14: 28
# 
# 5
# 1 3 1 3 1
# 
# 그리디 중에 특정 값을 만드는것과 같다.
# 여기서 핵심은 1 3 1 3 1 을 0 0 0 0 0 으로 만드는것이다.
# 
# 1 3 1 3 1
# -> if 3 % 1 == 
#
# input : 100,000 -> nlogn
# 


n = int(input())

l = list(map(int, input().split()))

count_2 = 0
count_1 = 0

for a in range(len(l)):
    if l[a] % 3 == 0:
        pass
    elif l[a] % 3 == 1:
        count_1 += 1
    elif l[a] % 3 == 2:
        count_2 += 1
    # elif l[a] % 2 == 0:
    #     count_2 += (l[a]//2)
    # elif l[a] % 2 == 1:
    #     count += (l[a]//2)+1

print(count_2, count_1)

if count_2 == count_1:
    print("YES")
else:
    print("NO")


# if count % 2 == 0:
#     print("YES")
# else:
#     print("NO")



