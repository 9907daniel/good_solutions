#
# 09:38 ~ 10:36
# 
# 입력 : 1000(파일수)*100(파일길이)
#
#
# 풀이법 : 일반 문자열 문제 같다
# 
#
# 1) split
# 2) lambda sort

def solution(files):
    numbers = ["1","2","3","4","5","6","7","8","9","0"]
    total = []
    for a in range(len(files)):
        l = list(files[a])
        number_pass = False
        number_index = []
        for b in range(len(l)):
            if l[b] in numbers and number_pass:
                # if b == len(l)-1:
                    # number_index.append(b)
                # elif l[b+1] not in numbers:
                number_index.append(b)
                
            elif l[b] in numbers and number_pass == False:
                number_pass = True
                number_index.append(b)
                
            # 반례 (런타임 에러) -> 왜냐하면 숫자가 Tail애도 다시 있을수 있으니
            if number_pass and l[b] not in numbers:
                break
                
        if len(number_index) >= 2:
            head = l[:number_index[0]]
            if number_index[1]+1 < len(l):
                number = l[number_index[0]:number_index[-1]+1]
                tail = l[number_index[-1]+1:]
            else:
                number = l[number_index[0]:]
                tail = []
        else:
            head = l[:number_index[0]]
            number = l[number_index[0]]
            
            if number_index[0]+1 < len(l):
                tail = l[number_index[0]+1:]
            else:
                tail = []
        joined_head = "".join(head)
        joined_number = "".join(number)
        lower_case_head = joined_head.lower()
        joined_tail = "".join(tail)
        
        j = [joined_head, lower_case_head, joined_number, int(joined_number), joined_tail]
        total.append(j)
    
        
    total.sort(key=lambda x:(x[1],x[3])) 
    answer = []
    for a in range(len(total)):
        s = total[a][0]+total[a][2]+total[a][-1]
        # if list(total[a][-1]) not in numbers:
        # s += total[a][-1]
        answer.append(s)
    return answer



