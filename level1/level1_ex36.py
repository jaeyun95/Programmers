#(36) 실패율

import operator

def solution(N, stages):
    answer = {}
    for stage in range(1,N+1):
        clear = 0
        not_clear = 0
        for user in stages:
            if user==stage: not_clear +=1
            if user>=stage: clear += 1
        if clear != 0: answer[stage] = not_clear / clear
        else: answer[stage] = 0
    return [value[0] for value in sorted(answer.items(), key=operator.itemgetter(1), reverse=True)]
		
# 다른 코드
'''
def solution(N, stages):
    answer = {}
    denominator = len(stages)
    for stage in range(1,N+1):
        if denominator != 0:
            count = stages.count(stage)
            answer[stage] = count/denominator
            denominator -= count
        else:
            answer[stage] = 0
    return sorted(answer, key=lambda x:answer[x], reverse=True)
'''