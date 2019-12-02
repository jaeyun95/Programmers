#(26) 포켓몬

def solution(nums):
    all_len = len(list(set(nums)))
    number = len(nums)//2
    if number >= all_len: return all_len
    else: return number

	
	
#다른 코드
'''
def solution(nums):
    return min(len(nums)/2, len(set(nums)))
'''