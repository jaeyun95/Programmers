#(34) 땅따먹기

def solution(land):
    answer = 0
    sum_list = [0]*4
    for row in land:
        pre_sum_lsit = sum_list[:]
        for i in range(len(row)):
            sum_list[i] = row[i] + max(pre_sum_lsit[i+1:] + pre_sum_lsit[:i])
    return max(sum_list)
