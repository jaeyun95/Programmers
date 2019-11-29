#(19) 최솟값 만들기

def solution(A,B):
    A.sort()
    B.sort(reverse=True)
    answer = 0
    for a,b in zip(A,B):
        answer += (a*b)
    return answer
	
	
#다른 코드
'''
def solution(A,B):
    return sum(a*b for a, b in zip(sorted(A), sorted(B, reverse = True)))
'''