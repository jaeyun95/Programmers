#(21) 자연수 뒤집어 배열로 만들기

def solution(n):
    answer = list(map(int, list(str(n))))
    answer.reverse()
    return answer
	

# 다른 코드
'''
def solution(n):
    return list(map(int, reversed(str(n))))
'''