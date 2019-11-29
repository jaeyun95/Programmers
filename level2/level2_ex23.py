#(23) JadenCase 문자열 만들기

def solution(s):   
    answer = ""
    for i,word in enumerate(s):
        answer += (word.upper() if (not i) or (i and s[i-1] == " ") else word.lower())
    return answer