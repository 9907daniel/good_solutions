# 11:33 ~ 12:00
# 입출력 : 100만이다 -> ON 로 풀어보자
#
# 전체 dictionary를 iterate 할때 모든 문자열의 글자까지 iterate 까지 iterate 한다면
# 20*1000000 -> 2천만
# 20! 
#
#
# 시간 복잡도 계산의 중요성@!


def solution(phone_book):
    
    dic = {}
    for a in range(len(phone_book)):
        # 인덕세를 기록해주자
        dic[phone_book[a]] = a
        
    for a in range(len(phone_book)):
        for b in range(len(phone_book[a])-1):
            current = phone_book[a][:b+1]
            if current in dic:
                return False
        if phone_book[a] in dic:
            if a != dic[phone_book[a]]:
                return False
    
    return True
                   
                   
                   
                   
                   
                   
                   
                   
                   
                   