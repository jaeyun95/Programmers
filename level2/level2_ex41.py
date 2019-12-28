#(41) 라면공장

import heapq
def solution(stock, dates, supplies, k):
    answer = 0
    heap = []
    date = 0
    while(stock < k):
        for index in range(date,len(dates)):
            if dates[index] <= stock:
                heapq.heappush(heap,-supplies[index])
                date = index + 1
            else: break
        stock += -heapq.heappop(heap)
        answer += 1
    return answer