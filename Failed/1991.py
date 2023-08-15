# 10:20 ~ 10:28 + 10:51 ~ 11:13


n = int(input())
# nodes = []
# start = ord('A')

# for a in range(n):
#     nodes.append(chr(start)+a)

    
dic = {}
for a in range(n):
    node, child_1, child_2 = input().split()
    dic[node] = [child_1, child_2]


results = ['A']
def dfs(start):
    l = dic[start]
    if l[0] != '.':
        results.append(l[0])
        dfs(l[0])
    if l[1] != '.':
        results.append(l[1])
        dfs(l[1])

dfs('A')    


# results_2 = []
# def dfs_2(start):
#     l = dic[start]
#     if l[0] != '.':
#         dfs(l[0])
#         results_2.append(start)
#     if l[1] != '.':
#         dfs(l[1])
#         results_2.append(start)
#     if l[0] == '.':
#         results_2.append(start)
#     if l[1] == '.':
#         results_2.append(start)

# dfs_2('A')
# print(results_2)  

# print(results)

# results_2 = []
# def dfs_2(start):
#     l = dic[start]
#     if l[0] != '.':
#         results.append(l[0])
#         dfs(l[0])
#     if l[1] != '.':
#         results.append(l[1])
#         dfs(l[1])
# dfs_2('A')    
# print(results_2)        
        
        
# l = dic[start]
# print(start)
# if l[0] != '.':
    
#     if dfs(l[0]):
#         results_2.append(start)
#         return True
# if l[1] != '.':
#     if dfs(l[1]):
#         results_2.append(start)
#         return True
# if l[0] == '.':
#     results_2.append(start)
#     return True
# if l[1] == '.':
#     results_2.append(start)
#     return True

