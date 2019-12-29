#(43) 가장 큰 정사각형 찾기

def solution(board):
    now = 0
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x]: 
                check = min([board[y][x-1],board[y-1][x],board[y-1][x-1]])
                if y and x and check: board[y][x] = check + 1
                now = max(board[y][x],now)
    return now**2