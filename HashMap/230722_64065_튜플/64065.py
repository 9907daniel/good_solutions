# 23:19 ~ 
# s의 길이가 100만이다
#
def solution(s):
    
    l = list(s)
    
    numbers = ["0","1","2","3","4","5","6","7","8","9"]
    
    results = {}
    tmp = []
    same_num = ""
    open_bracket = True
    same_number = True
    current_max = []
    
    # 처음 open, closing은 제외
    for a in range(1,len(l)-1):
        # "}"이 올때
        # "}" + "," 이 올떄
        if open_bracket == False and l[a] == ",":
            continue
        # "{"이 올떄
        if l[a] == "{":
            open_bracket = True
        # "{" + "," 이 올떄
        if l[a] in numbers and open_bracket:
            same_num += l[a]
        if l[a] == ',' and open_bracket:
            if int(same_num) in results:
                results[int(same_num)] += 1
            else:
                results[int(same_num)] = 1
            same_num = ""
            
        if l[a] == '}' and open_bracket:
            tmp.append(int(same_num))
            if int(same_num) in results:
                results[int(same_num)] += 1
            else:
                results[int(same_num)] = 1
            
            open_bracket = False
            same_num = ""
            tmp = []
    
    answer = []
    for a,b in sorted(results.items(), key=lambda x:x[1], reverse = True):
        answer.append(a)
    return answer
    
#     l = list(s)
    
#     numbers = ["0","1","2","3","4","5","6","7","8","9"]
    
#     results = []
#     tmp = []
#     same_num = ""
#     open_bracket = True
#     same_number = True
#     current_max = []
    
#     # 처음 open, closing은 제외
#     for a in range(1,len(l)-1):
#         # "}"이 올때
#         # "}" + "," 이 올떄

#         if open_bracket == False and l[a] == ",":
#             continue
        
#         # "{"이 올떄
#         if l[a] == "{":
#             open_bracket = True
        
#         # "{" + "," 이 올떄
#         if l[a] in numbers and open_bracket:
#             same_num += l[a]

#         if l[a] == ',' and open_bracket:
#             tmp.append(int(same_num))
#             same_num = ""
            
#         if l[a] == '}' and open_bracket:
#             tmp.append(int(same_num))
#             same_num = ""
#             results.append(tmp)
#             open_bracket = False
#             if len(tmp) > len(current_max):
#                 current_max = tmp[:] 
#             tmp = []
#     return current_max
    
            
            
            
            
            
            
            