#(9) 이중우선순위큐

import heapq
def solution(operations):
    heap = []
    for operation in operations:
        command, num = operation.split(' ')
        if command == 'I':
            heapq.heappush(heap,int(num))
        elif command == 'D' and len(heap) > 0:
            if num == '1':
                heap.pop(heap.index(heapq.nlargest(1,heap)[0]))
            else:
                heapq.heappop(heap)
    if len(heap) == 0: return [0,0]
    return [heapq.nlargest(1,heap)[0],heapq.nsmallest(1,heap)[0]]

#다른 코드
'''
def solution(operations):
    heap = []
    for operation in operations:
        command, num = operation.split(' ')
        if command == 'I':
            heap.append(int(num))
        elif command == 'D' and len(heap) > 0:
            if num == '1':
                heap.pop()
            else:
                heap.pop(0)
        heap.sort()
    if len(heap) == 0: return [0,0]
    return [max(heap),min(heap)]
'''