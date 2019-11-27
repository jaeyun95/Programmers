#(10) 멀쩡한 사각형

from fractions import gcd
def solution(w,h):
    if gcd(w,h) > 1: answer = w + h - gcd(w,h)
    else: answer = w+h-1
    return w*h - answer
	
	
#다른 코드
'''
from fractions import gcd
def solution(w,h):
    return w*h-w-h+gcd(w,h)
'''