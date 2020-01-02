#(46) 괄호 변환

def balance_check(p):
    check = 0
    for index,char in enumerate(p):
        if char == '(': check += 1
        else: check -= 1
        if check == 0: return index + 1
        
def right_check(u):
    check = [u[0]]
    for char in u[1:]:
        if len(check) == 0: return False
        if char == '(': check.append('(')
        else: check.pop()
    return True if not len(check) else False
     
def solution(p):
    if not p or right_check(p): return p
    u, v = p[:balance_check(p)], p[balance_check(p):]
    if right_check(u):
        answer = solution(v)
        return u + answer
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for index in range(len(u)):
            if u[index] == '(': u[index] = ')'
            else: u[index] = '('
        answer += ''.join(u)
        return answer