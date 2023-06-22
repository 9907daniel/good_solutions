# 13:33 - 
#
# 최대 : MM을 최대한 길개 가져간다
# 최소 : K를 그냥 5로 계속 추가한다
#
# 입력값 : 3000 미만
#
# 반례찾기
# MKMKMKMKMKMMM -> 5050505050100 / 1515151515100
# 5050505050100
# 1515151515100
#
#
#
#
#

l = list(input())

def get_max(l):
    
    result = ""
    current_m = 0
    
    for b,a in enumerate(l):
        if b == len(l)-1:
            if a == "M":
                # result += str(pow(10, current_m))
                print(current_m)
                tmp = "1"*current_m
                result += tmp
            elif a == "K":
                i = 5*pow(10, current_m)
                result += str(i)
            current_m = 0
        else:
            if a == "M":
                current_m += 1
            elif a == "K":
                i = 5*pow(10, current_m)
                result += str(i)
                current_m = 0       
    return int(result)
    
def get_min(l):
    
    result = ""
    current_m = -1
    
    for b,a in enumerate(l):
        if b == len(l)-1 and a == "M":
            current_m += 1    
            result += str(pow(10,current_m))
        else:
            if a == "M":
                current_m += 1
            elif a == "K":
                if current_m != -1:
                    result += str(pow(10,current_m))
                result += str(5)
                current_m = -1
    return int(result)
    
print(get_max(l))
print(get_min(l))