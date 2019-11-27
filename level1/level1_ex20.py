#(20) 이상한 문자 만들기

def solution(s):
    s = s.split(' ')
    for j,word in enumerate(s):
        word_list = list(word)
        for i in range(len(word_list)):
            if i%2 == 0: 
                word_list[i] = word_list[i].upper()
            else: 
                word_list[i] = word_list[i].lower()
        s[j] = ''.join(word_list)
    return ' '.join(s)
	

# 다른 코드
'''
def solution(s):
    s_list = s.split(' ')
    answer = []
    for word in s_list:
        after=''
        for i in range(0, len(word)):
            after += word[i].upper() if i%2 == 0 else word[i].lower()
        answer.append(after)
    return ' '.join(answer)
'''