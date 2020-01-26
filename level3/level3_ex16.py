#(16) [1차]추석 트래픽

def count(start, times):
    start = start
    end = start + 1000
    count = 0
    for time in times:
        if not (time[1] < start or time[0] >= end): count += 1
    return count

def solution(lines):
    answer = 0
    times = []
    for line in lines:
        time, demand = line.split()[1:]
        hh, mm, ss = time.split(':')
        time = int(hh)*3600*1000 + int(mm)*60*1000 + int(ss[:2]+ss[3:])
        demand = demand[:-1].split('.')
        if len(demand) > 1:
            demand = int(demand[0])*1000 + int(demand[1]+('0'*(3-len(demand[1]))))
        else: demand = int(demand[0])*1000
        times.append([time-demand+ 1, time])

    for time in times:
        now = max(count(time[0],times),count(time[1],times))
        if answer < now: answer = now
    return answer
	