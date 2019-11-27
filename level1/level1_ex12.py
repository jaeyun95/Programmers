#(12) 같은 숫자는 싫어

def solution(arr):
    answer = []
    for i,value in enumerate(arr):
        if value == arr[i]:
            if len(answer) == 0:
                answer.append(value)
            if answer[-1] != value:
                answer.append(value)
    return answer
	
	
# 다른 코드
'''
def solution(arr):
    answer = arr[:1]
    for value in arr:
        if answer[-1] == value:
            continue
        answer.append(value)
    return answer
'''