#(31) 점프와 순간 이동

def solution(n):
    if n%2 == 0: answer = 0
    else: answer = 1
    while n != 1:
        n = n//2
        if n%2 == 1: answer += 1
    return answer
	
#다른 코드
'''
def solution(n):
    return bin(n).count('1')
'''