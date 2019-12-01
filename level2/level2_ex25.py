#(25) 올바른 괄호

def solution(s):
    if not(s.count('(') == s.count(')')): return False
    s_list = list(s)
    s_check = []
    for s_word in s_list:
        if s_word == '(': s_check.append('(')
        elif s_word == ')': 
            if not s_check: return False
            else: s_check.pop()
    return True
	
	
#다른 코드
'''
def solution(s):
    x = 0
    for w in s:
        if x < 0:
            break
        x = x+1 if w=="(" else x-1 if w==")" else x
    return x==0
'''