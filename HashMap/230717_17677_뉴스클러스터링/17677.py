# 09:27 ~ 09:56
#
# 앞부분..? 
# 입력값 : 1000 
#
# 알고리즘 : 문자열 + 구현
#
# 해쉬맵을 통해 count를 관리할까..?

def solution(str1, str2):
    dic1 = {}
    dic2 = {}
    
    for a in range(len(list(str1))-1):
        if str1[a:a+2].isalpha() == False:
            continue
        if str1[a:a+2].lower() not in dic1:
            dic1[str1[a:a+2].lower()] = 1
        else:
            dic1[str1[a:a+2].lower()] += 1
            
    for a in range(len(list(str2))-1):
        if str2[a:a+2].isalpha() == False:
            continue
        if str2[a:a+2].lower() not in dic2:
            dic2[str2[a:a+2].lower()] = 1
        else:
            dic2[str2[a:a+2].lower()] += 1
    
    total_count = 0
    common_count = 0
    for a in dic1:
        if a in dic2:
            common_count += min(dic1[a], dic2[a])
            total_count += max(dic1[a],dic2[a])
        else:
            total_count += dic1[a]

    for b in dic2:
        if b not in dic1:
            total_count += dic2[b]
    
    if total_count == 0:
        return 65536
    if common_count == 0:
        return 0
    
    return (int((common_count / total_count)*65536))
        
    
    