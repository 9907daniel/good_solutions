from itertools import combinations

def solution(weights):
    dic = {}
    
    for a in weights:
        if a in dic:
            dic[a] += 1
        else:
            dic[a] = 1
    
    answer = 0
    for a in dic:
        # if there are more than one of the same..
        if dic[a] > 1:
            answer += dic[a]-1
        
        if a*(1/2) in dic:
            answer += min(dic[a], dic[a*(1/2)])
        if a*(3/4) in dic:
            answer += min(dic[a], dic[a*(3/4)])
        if a*(2/3) in dic:
            answer += min(dic[a], dic[a*(2/3)])

    print(answer)
    
    
    
    
#     seats = [1,2,3,4]
#     graph = [[] for _ in range(len(weights))]
    
#     for a in range(len(weights)):
#         for b in seats:
#             graph[a].append(weights[a]*b)
    
#     print(graph)
    
#     for a in range(len(graph)):
#         for b in range(a+1, len(graph)):
#             if graph[a] in graph[]
    
    
    # def balance(x,y):
#         for a in seats:
#             for b in seats:
#                 if a*x == b*y:
#                     return True
    
#     count = 0
#     # for a in combinations(weights,2):
#     for a in range(len(weights)):
#         for b in range(a+1, len(weights)):
#             if balance(weights[a],weights[b]):
#                 count += 1
#     return count
    
    
            
    
    