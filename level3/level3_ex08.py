#(8) 멀리 뛰기

def solution(n):
    if n < 3: return n
    value1, value2 = 1, 2
    for i in range(3,n+2):
        value1, value2 = value2, value1 + value2
    return value1%1234567