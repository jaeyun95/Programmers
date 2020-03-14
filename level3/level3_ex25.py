#(25) 디스크 컨트롤러

import heapq
def solution(jobs):
    answer, now, count, number = 0, 0, 0, len(jobs)
    end = -1
    waiting = []
    while(count < number):
        for job in jobs[:]:
            if end < job[0] <= now:
                answer += (now-job[0])
                heapq.heappush(waiting,job[1])
        if len(waiting) > 0:
            answer += len(waiting)*waiting[0]
            end = now
            now += heapq.heappop(waiting)
            count += 1
        else: now += 1
    return answer//number