# 19:06 ~ 19:50 + 20:29 ~ 
# 
# 입출력)
# 문자열 길이 = 100만 -> 탐삭은 big N
# 
# 
# 가능할듯한 알고리즘)
# 그리디, 브루트 포스, 투포인터
#
# 풀이)
# 어떻게 하면 100만을 TLE없이 순회할까 
#
#
# 풀이1) - NlogN -> TLE
# 풀이2) - 자료구조를 활용하면 좋을꺼 같다...
# {{}}{}{}}} 문제와 유사한 느낌으로..?
#  -> 한번의 Nlog으로 풀이할 방법이..
#  중요 포인트 -> stack를 활용해서 맨 안에부터 제거를 해야한다
#           -> 
#

l = list(input())
bomb = list(input())
q = []

first_letter = bomb[0]
last_letter = bomb[-1]

for a in range(len(l)):
    q.append(l[a])
    if l[a] == last_letter and 0<= len(q)-len(bomb):
               
        tmp = "".join(q[len(q)-len(bomb):])
        if tmp == "".join(bomb):
            for _ in range(len(bomb)):
                q.pop()
            # q = q[:len(q)-len(bomb)]

if len(q) == 0:
    print("FRULA")
else:
    answer = "".join(q)
    print(answer)
    
    
################################################################
################################################################   
# l = list(input())
# bomb = list(input())
# q = []

# first_letter = bomb[0]
# last_letter = bomb[-1]

# for a in range(len(l)):
#     q.append(l[a])
#     if l[a] == last_letter and 0<= len(q)-len(bomb):
#         current = len(q)-1
#         count = 0
#         for b in range(len(bomb)-1,-1,-1):
#             if bomb[b] == q[current]:
#                 current -= 1
#                 count += 1
#             else:
#                 break
#         if count == len(bomb):
#             q = q[:len(q)-len(bomb)]

# if len(l) == 0:
#     print("FRULA")
# else:
#     answer = "".join(q)
#     print(answer)

# ################################################################
# ################################################################
    
    
# l = list(input())
# bomb = list(input())
# start = 0
# while True:
#     current = 0
#     tmp = start
#     reverse = False
#     if l[start] == bomb[current]:
#         while current < len(bomb) and tmp < len(l):   
#             if l[tmp] != bomb[current]:
#                 break
#             current += 1
#             tmp += 1
#         if current == len(bomb):
#             left,right = l[:start], l[tmp:]
#             l=left+right
#             start = 0
#             reverse = True
    
#     if len(l) < len(bomb):
#         break
#     if reverse != True:
#         start += 1
#     if start >= len(l):
#         break
# if len(l) == 0:
#     print("FRULA")
# else:
#     answer = "".join(l)
#     print(answer)