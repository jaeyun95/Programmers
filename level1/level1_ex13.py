#(13) 두 정수 사이의 합

def solution(a, b):
    if a == b : return a
    elif a > b : 
        return ((a+b)*(abs(a-b)//2))+((a+b)//2) if abs(a-b)%2 == 0 else (a+b)*(abs(a-b)//2 + 1)
    else : 
        return ((a+b)*(abs(b-a)//2))+((a+b)//2) if abs(b-a)%2 == 0 else (a+b)*(abs(b-a)//2 + 1)
	
	
# 다른 코드
'''
def solution(a, b):
    if a > b : a, b = b, a
    return sum(list(range(a,b+1)))

'''