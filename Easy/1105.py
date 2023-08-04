# 09:57 ~ 10:08
# 입력 : 2억 -> DP, Greedy, Binary Search
#
#
#
# 문제) L<= x <=R 중에 8이 가장 적게 들어간다..?
#
#
# 1) 숫자 중, 앞부터 같은 자릿수를 세주자 (8일때)
# 2) 서로 뺴줘서 차이 비교 (8 이하이면 +1 해야할수도)
#
#
# 8810 8819 -> 2
# 8818
#
#
#..? 이상한 문제

l,r = map(int, input().split())

count = 0

tmp_1 = list(str(l))
tmp_2 = list(str(r))

if len(tmp_1) != len(tmp_2):
    print(0)
else:
    for a in range(len(tmp_1)):
        if tmp_1[a] == '8' and tmp_2[a] == '8':
            count += 1
        elif tmp_1[a] != tmp_2[a]:
            break
    difference = r-l
    print(count)
    