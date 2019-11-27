#(5) 나누어 떨어지는 숫자 배열

def solution(arr, divisor):
    answer = []
    for value in arr:
        if (value%divisor) == 0:
            answer.append(value)
    if len(answer) == 0:
        answer.append(-1)
    return sorted(answer)
	
	
# 다른 코드
'''
def solution(arr, divisor):
    answer = [i for i in arr if not i % divisor]
    return sorted(answer) if len(answer) else [-1]
'''