#(15) 종이접기

def solution(n):
    answer = [0]
    for i in range(n-1):
        answer = [j for sub in list([0] + [answer[i]] + [1] if i%2 == 0 else [answer[i]] for i in range(len(answer))) for j in sub]
    return answer
	
#다른 풀이
'''
def solution(n):
    answer = [0]
    for i in range(1,n):
        k = [1-j for j in answer]
        answer = answer + [0] + k[::-1]

    return answer
'''