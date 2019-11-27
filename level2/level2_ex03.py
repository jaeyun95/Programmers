#(3) 124 나라의 숫자

def solution(n):
    answer = ''
    while n :
        n, share = divmod(n, 3)
        answer = str(share) + answer
        if not share: n -= 1
    answer = answer.replace('0','4')
    return answer
	

#다른 코드
'''
def solution(n):
    answer = ''
    while n > 0 :
        n -= 1
        answer = '124'[n%3] + answer
        n //= 3
    return answer
'''