#(19) 시저 암호

def solution(s, n):
    s_list = list(s)
    for i,alpha in enumerate(s_list):
        if alpha == ' ': continue
        if alpha.islower():
            if ord(alpha) + n > ord('z'):
                s_list[i] = chr(ord(alpha)+n-(ord('z')-ord('a')+1))
            else:
                s_list[i] = chr(ord(alpha)+n)
        elif alpha.isupper():
            if ord(alpha) + n > ord('Z'):
                s_list[i] = chr(ord(alpha)+n-(ord('Z')-ord('A')+1))
            else:
                s_list[i] = chr(ord(alpha)+n)
    return ''.join(s_list)
	

# 다른 코드
'''
def solution(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i])-ord('A')+n)%26+ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i])-ord('a')+n)%26+ord('a'))
    return ''.join(s)
'''