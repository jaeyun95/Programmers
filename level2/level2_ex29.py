#(29) 지어 제거하기

def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if(answer[-1] == i):
                answer.pop()
            else:
                answer.append(i)    
    return not(answer)
	
	
#다른 코드
'''
from collections import deque
def solution(s):
    index = 0
    answer_stack = []
    s = deque(list(s))
    while s:
        if len(answer_stack) == 0: 
            answer_stack.append(s.popleft())
        elif answer_stack[-1] == s[0]: 
            answer_stack.pop()
            s.popleft()
        else: answer_stack.append(s.popleft())
    return 1 if len(answer_stack)==0 else 0
'''