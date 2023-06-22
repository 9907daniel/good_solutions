# 1:45~ 2:06 + 2:58 ~ 
#
# 입출력 : 최대 15
# 알고리즘 : queue, backtrack, 힙, 와타툼, 구현=> 백트래킹은 아닌듯
#
# 목적 : 모든 판들을 옮겨 가장 큰거를 3번 가장 밑에 있겠금..
#
# 일단 모든 조합을 구한다 -> 만약 무거운게 이미있었다면 pass
#


# 하노이의 탑은 재귀함수로 풀수 있는전형적인 문제
# 1. n개의 원판을 옮기기 위해서는 n-1개의 원판을 중간으로 옮겨야함
# 2. 이후 n번쨰 원판을 목적지로 옮겨야함
# 3. 다시 1,2번 단계를 n-1만큼 실행
#
#

def solutions(n):

    results = []
    
    def hanoi(start, end, midpoint, n):
        if n ==1:
            results.append([start,end])
        else:
            
            # 목적지가 안닌것들을 시작 -> 중간으로
            hanoi(start, midpoint, end, n-1)
            
            # 현재 가장 작은것을 목적지에 넣어다
            hanoi(start, end, midpoint, 1)
            
            # 중간 -> 끝으로 옮겨준다
            hanoi(midpoint, end, start, n-1)
        
        
    # 1에서 3으로 옮기고 중간 지점을 2로 한다
    hanoi(1,3,2,n)




# from collections import deque

# def combi(q, n, steps):
#     if len(q[0]) == 0 and len(q[1]) == 0:
#         return
#     print(q)
#     for a in range(3):
#         x = q[a].pop()
#         for b in range(3):
#             if b != a and min(q[b]) > x:            
#                 q[b].append(x)
#                 combi(q,n,steps+1)
#                 q[b].pop()
                


# def solution(n):
#     # 1~n까지 들어 있는 배열을 만든다
#     l = [a for a in range(n,0,-1)]  # 4,3,2,1
    
    
#     # 재귀함수를 사용해 원판을 계속해서 옮겨 모든 조합을 구한다
#     # 만약 이미 무거운것이 들어 있다면 return False
    
#     q = [l,[],[]]
#     combi(q, n, 0)
    