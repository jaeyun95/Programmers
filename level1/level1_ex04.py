#(4) 가운데 글자 가져오기

def solution(s):
    # 문자열의 길이가 홀수일 경우
    if len(s)%2==1:
        return s[len(s)//2]
    # 문자열의 길이가 짝수일 경우
    else:
        return s[len(s)//2-1:len(s)//2+1]
	
	
# 다른 코드
'''
def solution(s):
    mid = len(s)//2
    return s[mid] if len(s)%2 else s[mid-1:mid+1]
'''