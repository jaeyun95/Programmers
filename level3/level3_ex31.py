#(31) N-Queen

count = 0
def check(col,n):
    for i in range(n):
        if (col[n] in col[:n]) or (abs(col[n]-col[i]) == abs(n-i)): return False
    return True

def nqueen(col,n):
    global count
    if len(col) == n: 
        count += 1
    else:
        for i in range(len(col)):
            col[n] = i
            if check(col,n):
                nqueen(col,n+1)

def solution(n):
    col = [0]*n
    nqueen(col,0)
    return count