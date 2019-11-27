#(27) x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    if x > 0:
        answer = [num for num in range(x,x*n+1,x)]
    elif x < 0:
        answer = [num for num in range(x,x*n-1,x)]
    else:
        answer = [0]*n
    return answer
	
# 다른 코드
'''
def solution(x, n):
    return [x*i for i in range(1, n+1)]
'''