#(6) 문자열 내 마음대로 정렬하기

import operator

def solution(strings, n):
    new_string = {}
    answer = []
    # index값의 문자를 가장 앞으로 뺌(단어 알파벳 순서 재정렬)
    for word in strings:
        new_word = word[n]+word[:n]+word[n+1:]
        new_string[word] = new_word
        
    # 전체 단어 정렬(value를 기준으로 정렬)
    pre_answer = sorted(new_string.items(), key=operator.itemgetter(1))
    
    # 딕셔너리 --> 리스트로 변환
    for ans in pre_answer:
        answer.append(ans[0])
    return answer
	
	
# 다른 코드
'''
def solution(strings, n):
    return sorted(sorted(strings), key=lambda x: x[n])
	
	or
	
import operator

def solution(strings, n):
    return sorted(sorted(strings), key=operator.itemgetter(n))
'''