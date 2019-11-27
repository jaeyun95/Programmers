#(25) 정수 내림차순으로 배치하기

def solution(n):
    answer = sorted(list(map(int,list(str(n)))),reverse=True)
    return int(''.join(list(map(str,answer))))
	
# 다른 코드
'''
def solution(n):
    return int(''.join(sorted(str(n),reverse=True)))
'''