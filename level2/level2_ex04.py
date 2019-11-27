#(4) 프린터

import operator

def solution(priorities, location):
    print_queue = [(chr(65+i),importance) for i, importance in enumerate(priorities)]
    target = chr(65+location)
    answer = 0
    while True:
        if print_queue[0][1] < max(print_queue, key = operator.itemgetter(1))[1]:
            change = print_queue[0]
            print_queue.remove(change)
            print_queue.append(change)
        else: 
            output = print_queue[0][0]
            print_queue.remove(print_queue[0])
            answer += 1
            if target == output: break
    return answer