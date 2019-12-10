#(33) 예상 대진표

def solution(n,a,b):
    answer = 0
    while True:
        if a == b: return answer
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

	
#다른 코드
'''
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
'''