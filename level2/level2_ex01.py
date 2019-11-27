#(1) 완주하지 못한 선수

def solution(arrangement):
    answer = 0
    stick_stack = []
    for value in arrangement.replace('()','*'):
        if value == '(' : 
            answer += 1
            stick_stack.append(value)
        elif value == ')' : stick_stack.pop()
        else : answer += len(stick_stack)
    return answer