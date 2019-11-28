#(17) 더 맵게

import heapq

def solution(scoville, K):
    answer = 0
    scoville_heap = []
    for value in scoville: heapq.heappush(scoville_heap,value)
    while scoville_heap[0] < K:
        if len(scoville_heap) < 2: return -1
        heapq.heappush(scoville_heap, (heapq.heappop(scoville_heap) + (heapq.heappop(scoville_heap)*2)))
        answer+=1
    return answer