#(6) 2xn타일링

def solution(n):
    value1, value2 = 1, 1
    for i in range(n):
        value1, value2 = value2, value1+value2
    return value1%1000000007