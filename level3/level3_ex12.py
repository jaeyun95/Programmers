#(12) 거스름돈

def solution(n, money):
    answer = 0
    count_table = [[1 if i == 0 and j%money[0] == 0 else 0 for j in range(n+1)] for i in range(len(money))]
    for i in range(1, len(money)):
        for j in range(n+1):
            if j >= money[i]:
                count_table[i][j] = (count_table[i-1][j]+count_table[i][j-money[i]])
            else:
                count_table[i][j] = count_table[i-1][j]
    return count_table[-1][-1]%1000000007
