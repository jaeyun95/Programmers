#(32) 하샤드 수

def solution(x):
    x_sum = sum(list(map(int,list(str(x)))))
    return True if x%x_sum == 0 else False
	
# 다른 코드
'''
def solution(x):
    return x % sum(int(n) for n in str(x)) == 0
'''