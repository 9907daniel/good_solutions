# 
# 우선 위/아래를 결정하는것은 쉽다
# 문제는 왼쪽 / 오른쪽으로 이동하는 방법을 구하는게 복잡하다
# 왼쪽 / 오른쪽을 지금 당장 다음 차례로 가기 위해 A의 최소 회수 방향으로 간다고 접근을 했는데..
# ABBBBBBBAAAAAAAAABAA
# 같은 경우 왼른쪽으로 시작을 하지만, 사실 왼쪽으로 가는것이 더 맞다.
# 그렇기 때문에 현재 시점에서 가장 가까운것을 찾는것이 아닌, 전체에서 가장 많은 A를 고려해야한다


def solution(name):    





# def solution(name):    
#     new_name = [a for a in name]
    
#     check = 0
#     for a in new_name:
#         if a != "A":
#             check +=1 
    
#     count = 0
#     previous = 0
#     consecutive_a = 0
#     a = 0
    
    
#     if check == 1:
#         a= 0
#         for a in range(1):
#             positive_count = 1
#             for c in range(previous+1,len(new_name)):
#                 if new_name[c] != "A":
#                     positive = c
#                     break
#                 positive_count += 1
#             negative_count = 1
#             for d in range(len(new_name)-1,-1,-1):
#                 if new_name[d] != "A":
#                     negative = d
#                     break
#                 negative_count += 1

#             if positive_count > negative_count+previous:
#                 count += negative_count+previous
#                 previous = negative
#             else:
#                 count += positive_count
#                 previous = positive
    
#             if ord(new_name[previous])-ord("A") > 13:
#                 count += abs(ord("Z")-ord(new_name[previous])+1)

#             else:
#                 count += abs(ord("A")-ord(new_name[previous]))
#         a += 1
    
    
#     # current
    
#     while a <= check-1:        
#         if a != 0:
#             positive_count = 1
#             for c in range(previous+1,len(new_name)):
#                 if new_name[c] != "A":
#                     positive = c
#                     break
#                 positive_count += 1
#             negative_count = 1
#             for d in range(len(new_name)-1,-1,-1):
#                 if new_name[d] != "A":
#                     negative = d
#                     break
#                 negative_count += 1

#             if positive_count > negative_count+previous:
#                 count += negative_count+previous
#                 previous = negative
#             else:
#                 count += positive_count
#                 previous = positive
    
#         if ord(new_name[previous])-ord("A") > 13:
#             count += abs(ord("Z")-ord(new_name[previous])+1)
#             # print(abs(ord("Z")-ord(new_name[previous])+1))
#         else:

#             count += abs(ord("A")-ord(new_name[previous]))
#             print(abs(ord("A")-ord(new_name[previous])))
#         a += 1
    
#     return count


        
# #         if a == "A":
# #             consecutive_a += 1
# #             continue
                
# #         if b-previous > len(new_name)-b:
# #             count += len(new_name)-b
# #         else:
# #             count += b-previous
        
    
        
# #         consecutive_a = 0
# #         previous = b
        
        
                