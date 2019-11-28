#(18) 피보나치 수

def solution(n):
    first = 0
    second = 1
    for i in range(n):
        first, second = second, first + second
    return first%1234567
	
	
#다른 코드
'''
def solution(n):
    first = 0
    second = 1
    for i in range(n):
        third = first + second
        first = second
        second = third
    return first%1234567

'''