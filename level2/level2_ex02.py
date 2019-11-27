#(2) 기능개발

import math
def solution(progresses, speeds):
    distribution = [math.ceil((100-value)/speed) for value,speed in zip(progresses,speeds)]
    answer = []
    pivot = 0
    number = 1
    for i in range(1,len(distribution)):
        if distribution[pivot] >= distribution[i]: 
            number += 1
            continue
        answer.append(number)
        number = 1
        pivot = i
    answer.append(number)
    return answer
	

#다른 코드
'''
import math
def solution(progresses, speeds):
    answer = []
    progresses = [math.ceil((100-a)/b) for a, b in zip(progresses, speeds)]
    front = 0
    for idx in range(len(progresses)):
        if  progresses[front] < progresses[idx]:
            answer.append(idx-front)
            front = idx
    answer.append(len(progresses)-front)
    return answer
'''