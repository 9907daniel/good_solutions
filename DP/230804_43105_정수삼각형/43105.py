# 10:17 ~ 10:37
#
#
# 풀이 1) 그냥 BFS / DFS -> TLE
# 풀이 2) DP
    

def solution(triangle):
    dp = [[0]*len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    
    for a in range(1, len(triangle)):
        for b in range(len(triangle[a])):
            if 0<= b-1:
                dp[a][b] = triangle[a][b]+max(dp[a-1][b], dp[a-1][b-1])
            else:
                dp[a][b] = triangle[a][b]+dp[a-1][b]

    return max(dp[-1])    
    
    
    
    
    
    
    
    
    
#     q = deque()
#     q.append((0,0,triangle[0][0]))
    
#     largest = 0
#     while q:
#         x,y,count = q.popleft()
        
#         nx = x+1
#         ry = y+1
        
#         if nx < len(triangle):
#             q.append((nx,y,count + triangle[nx][y]))
#             if ry < len(triangle[nx]):
#                 q.append((nx,ry,count + triangle[nx][ry]))
        
#         largest = max(largest, count)
#     return largest
    
    
    
    
    
    
    
    
    