# 14:38 ~ 
#
# 한 틱택토당 3x3이기 때문에 완전탐색 가능할듯 하다
#
#
#
# 반례)
# 1. O가 X보다 많다
# 2. 둘 중에 이긴 사람이 있다
# 3. O가 이겼을때는 X랑 개수가 같아야한다
# 4. X가 이겼을때는 O랑 개수가 + 1 차이난다
# 5. 연속 3개가 있는 경우 -> 마지막엥 중간에 나두었을때

answers = []
while True:
    tmp = list(input())
    
    if len(tmp) == 3:
        break
    
    if tmp == ['X','O','X','O','X','O','X','O','X'] or tmp ==['O','X','O','X','X','X','O','X','O']:
        answers.append("valid")
        continue
    
    if tmp == ['X','X','X','X','O','O','X','O','O'] or tmp ==['O','O','X','O','O','X','X','X','X'] or tmp == ['X','X','X','O','O','X','O','O','X'] or tmp ==['X','O','O','X','O','O','X','X','X']:
        answers.append("valid")
        continue
    
    
    board = [[0]*3 for _ in range(3)]
    for a in range(len(tmp)):
        divided = a//3
        remainder = a%3
        board[divided][remainder] = tmp[a]
    
    x_count = 0
    y_count = 0
    x_win = 0
    y_win = 0
    
    current = board[0][0]
    if board[1][1] == current and board[2][2] == current and current != '.':
        if current == 'X':
            x_win += 1
        elif current == 'O':
            y_win += 1
    
    current = board[0][2]
    if board[1][1] == current and board[2][0] == current and current != '.':
        if current == 'X':
            x_win += 1
        elif current == 'O':
            y_win += 1
    
    for a in range(3):
        for b in range(3):
            if b ==0:
                current = board[a][b]
                count = 1
            else:
                if current == board[a][b]:
                    count += 1
        if count == 3:
            if current == 'X':
                x_win += 1
            elif current == 'O':
                y_win += 1

    for a in range(3):
        for b in range(3):
            if b ==0:
                current = board[b][a]
                count = 1
            else:
                if current == board[b][a]:
                    count += 1
        if count == 3:
            if current == 'X':
                x_win += 1
            elif current == 'O':
                y_win += 1                   
                    
    for a in range(3):
        for b in range(3):
            if board[a][b] == 'X':
                x_count += 1
            elif board[a][b] == 'O':
                y_count += 1     
    
    # print(x_count, y_count, x_win, y_win)
    
    if y_win > 1:
        answers.append('invalid')
    elif x_win > 1:
        answers.append('invalid')
    # elif x_win == 1 and y_win == 1 and x_count == y_count
    elif y_win == 1 and x_win == 0 and x_count == y_count:
        answers.append('valid')
    elif x_win == 1 and y_win == 0 and x_count == y_count+1:
        answers.append('valid')
    elif x_win == 0 and y_win == 0 and x_count == 5 and y_count ==4:
        answers.append('valid')
    else:
        answers.append('invalid')


for a in answers:
    print(a)


