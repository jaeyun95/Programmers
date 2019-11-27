#(18) 약수의 합

def solution(n):
    return sum([num for num in range(1,n+1) if n%num == 0])