#(13) 등굣길

def solution(m, n, puddles):
    answer = [[0 for _ in range(m)] for _ in range(n)]
    answer[0][0] = 1
    for i in range(n):
        for j in range(m):
            if (i == 0 and j == 0) or ([j+1,i+1] in puddles): continue
            else: answer[i][j] = answer[i-1][j] + answer[i][j-1]
    return answer[n-1][m-1]%1000000007
