#(21) 최댓값과 최솟값

def solution(s):
    s_list = s.split(' ')
    s_list = list(map(int,s_list))
    return str(min(s_list))+' '+str(max(s_list))
	
	
#다른 코드
'''
def solution(s):
    s = list(map(int,s.split()))
    return str(min(s)) + " " + str(max(s))
'''