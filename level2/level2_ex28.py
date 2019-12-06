#(28) 소수 만들기

def solution(nums):
    answer = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            for k in range(j+1,len(nums)):
                sum_num = nums[i] + nums[j] + nums[k]
                check = 0
                for idx in range(1,sum_num+1):
                    if sum_num%idx == 0: check += 1
                    if check > 2:  break
                if check == 2: 
                    answer += 1
    return answer
	
	
#다른 코드
'''
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
'''