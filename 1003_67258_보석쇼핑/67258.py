# 20:17 ~ 
#
# 입출력) 100,000 이다
#
# 알고리줌) 얼핏 봤을때 해쉬맵 + 누적합을 사용하면 어떨까 싶다
#
# 1) 모든 종류를 기록해줘야한다 set에 추가하여, len() 관리
# 2) 탬색을 하며 set의 길이만큼 dic가 길어진다면 
#    여기서 dic = 0이 되면 key-value를 자동으로 삭제해 주자, 그리고 종류의 개수는 매번 확인하지말고..? 따라 관리해주자..?
#    len(dic) = Big1 ..? 인가..?
#
# 누적합을 할때 start, start+1을 한다면 시간복잠조가 높을꺼 같다..
# 차라리 투포인터를 화용하는게 더 좋을까..?
#
#
# 1번 순환을 해서 가장 먼저 나오는 조합을 정하고... 이를 기준으로 모든 GEM이 포함되어 있어도.. 길이가 줄 update
#
#
# 문제 핵심 : 한번 좁혀 나간거는 다시 늘릴필요가 없다..
#

def solution(gems):
    record = set(gems)  
    dic = {}
    # 전범위는 무조건 보석을 전부 포함하고 있으니까 답이될수도 있다
    answer = [0, len(gems) - 1] 
    left = 0
    
    # 뒤에를 쭉~~ 추가해주다가
    # 전부 포함하는 순간푸터 앞에를 제거해주고 가능한지 봐준다.. 
    for right in range(len(gems)):
        # set랑 차있을때까지 추가
        if gems[right] not in dic:
            dic[gems[right]] = 1
        else:
            dic[gems[right]] += 1
        
        while len(dic) == len(record):
            # 차이가 보다 작다면 최신화..
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
            
            # 맨 앞에 제거해주기..
            dic[gems[left]] -= 1
            if dic[gems[left]] <= 0:
                dic.pop(gems[left])
            left += 1
            
    return [answer[0] + 1, answer[1] + 1]  
   
    
    
        
        
    