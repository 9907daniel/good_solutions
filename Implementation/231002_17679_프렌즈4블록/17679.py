# 20:00 ~20:35
# 
# 1) 탐색을 하면서 모든 2x2를 찾는다,
# 1-1) 중요!!!! - 모든 2x2붙어있는것을 찾아 줄 필요 없이, 한번 순환만 하면 된다..
# 2) BFS 를 사용하면서 모든 2x2를 찾느다
# 3) 전부 제거
#

from collections import deque

def square(a,b,board,remove):
    current = board[a][b]
    if board[a+1][b] == current and board[a][b+1] == current and board[a+1][b+1] == current and board[a+1][b] != '.':
        remove.append([a,b])
        remove.append([a+1,b])
        remove.append([a+1,b+1])
        remove.append([a,b+1])
        return remove
    else:
        return False

def solution(m, n, board):
    board = [list(a) for a in board]
    
    total = 0
    while True:
        remove = []
        did_pop = False
        # 맨마지막에는 어차피 벽이니까 len()-1까지 확인
        for a in range(len(board)-1):
            for b in range(len(board[a])-1):
                check = square(a,b,board,remove)
                if check != False:
                    remove = check
                    did_pop = True
        for a in remove:
            if board[a[0]][a[1]] != '.':
                total += 1
                board[a[0]][a[1]] = '.'

        for a in range(len(board[0])):
            pull_gravity = False
            q = deque()
            index = -1
            for b in range(len(board)-1,-1,-1):
                if board[b][a] == '.':
                    pull_gravity = True
                    index = max(b, index)
                else:
                    if pull_gravity:
                        q.append(board[b][a])
            if pull_gravity:
                count = len(q)
                for b in range(index,-1,-1):
                    if count != 0:
                        x = q.popleft()
                        board[b][a] = x
                        count -= 1
                    else:
                        board[b][a] = '.'

        if did_pop == False:
            break

    return total
    
    # [['T', 'T', 'T', 'A', 'N', 'T'], 
    #  ['.', '.', 'F', 'A', '.', '.'], 
    #  ['.', '.', '.', 'F', '.', '.'],
    #  ['T', '.', '.', 'R', 'A', 'A'], 
    #  ['T', 'T', 'M', 'M', 'M', 'F'], 
    #  ['T', 'M', 'M', 'T', 'T', 'J']]

    
    # [['.', '.', '.', 'A', '.', '.'],
    #  ['.', '.', '.', 'A', '.', '.'], 
    #  ['T', '.', 'T', 'F', 'N', 'T'], 
    #  ['T', 'T', 'F', 'R', 'A', 'A'], 
    #  ['T', 'T', 'M', 'M', 'M', 'F'], 
    #  ['T', 'M', 'M', 'T', 'T', 'J']]
    
    # ['.', '.', '.', 'A', '.', '.'], 
    # ['.', '.', '.', 'A', '.', '.'],
    # ['.', '.', 'T', 'F', 'N', 'T'],
    # ['.', '.', 'F', 'R', 'A', 'A'],
    # ['T', '.', 'M', 'M', 'M', 'F'], 
    # ['T', 'M', 'M', 'T', 'T', 'J']]
    
    
    
    
    
    