#(22) 정수 제곱근 판별

import math
def solution(n):
    if not math.sqrt(n).is_integer():
        return -1
    return (math.sqrt(n)+1)**2
	

# 다른 코드
'''
import math
def solution(n):
    if not math.sqrt(n).is_integer():
        return -1
    return pow((math.sqrt(n)+1),2)
'''