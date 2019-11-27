#(9) 수박수박수박수박수박수?

def solution(n):
    if n%2==0:
        return "수박"*(n//2)
    return "수박"*(n//2)+"수"
	
	
# 다른 코드
'''
def solution(n):
    return "수박"*(n//2) + "수"*(n%2)
'''