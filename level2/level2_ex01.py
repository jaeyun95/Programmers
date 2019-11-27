#(1) 쇠막대기

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