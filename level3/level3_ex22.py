#(22) 저울

def solution(weight):
    weight.sort()
    if weight[0] != 1: return 1
    answer = weight[0]
    for number in weight:
        if answer >= number:
            answer += number
        else: break
    return answer