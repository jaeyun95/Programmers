#(50) 수식 최대화

priority_list = [["+","-","*"],["+","*","-"],["-","+","*"],
                 ["-","*","+"],["*","-","+"],["*","+","-"]]
def cal(number, operator, priority):
    while priority:
        now = priority.pop(0)
        while now in operator:
            index = operator.index(now)
            operator.pop(index)
            left = number.pop(index)
            right = number.pop(index)
            result = eval(str(left)+now+str(right))
            number.insert(index,result)
    return number[0]

def solution(expression):
    number, operator = [], []
    num = ""
    for n in expression:
        if n in "+-*":
            operator.append(n)
            number.append(int(num))
            num = ""
        else: num += n
    number.append(int(num))

    answer = 0
    for priority in priority_list:
        answer = max(abs(cal(number[:],operator[:],priority)),answer)
    return answer