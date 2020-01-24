#(17) 최고의 집합

def solution(n, s):
    if s-n < 0: return [-1]
    value, remainder = divmod(s,n)
    answer = [value]*(n-remainder) + [value+1]*remainder
    return answer