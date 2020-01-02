#(45) [1차]프렌즈4블록

def fill_blank(board):
    for col in range(len(board[0][:])):
        for row in range(len(board)-1,-1,-1):
            if board[row][col] == '0':
                for search_row in range(row-1,-1,-1):
                    if board[search_row][col] != '0':
                        board[row][col], board[search_row][col] = board[search_row][col], board[row][col]
                        break
    return board

def delete_block(board,delete_list):
    for delete_value in delete_list:
        board[delete_value[0]][delete_value[1]] = '0'
    return board

def find_block(board):
    delete_list = []
    for row in range(len(board)-1):
        for col in range(len(board[0])-1):
            if (board[row][col] != '0') and (board[row][col] == board[row+1][col] == board[row+1][col+1] == board[row][col+1]):
                delete_list += [(row,col)]
                delete_list += [(row+1,col)]
                delete_list += [(row+1,col+1)]
                delete_list += [(row,col+1)]
    return list(set(delete_list))

def solution(m, n, board):
    board = [[block for block in row] for row in board]
    while True:
        delete_list = find_block(board)
        if not delete_list: break
        delete_block(board,delete_list)
        fill_blank(board)
    answer = [row.count('0') for row in board]
    return sum(answer)