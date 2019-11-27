#(30) 최대공약수 최소공배수

def solution(n, m):
    n_list = [num for num in range(1,n+1) if n%num==0]
    m_list = [num for num in range(1,m+1) if m%num==0]
    max_list = list(set(n_list) & set(m_list))
    return [max(max_list),n*m/max(max_list)]
	
# 다른 코드
'''
from fractions import gcd
def solution(n, m):
    return [gcd(n,m),n*m/gcd(n,m)]
'''