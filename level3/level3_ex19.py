#(19) 기지국 설치

def solution(n, stations, w):
    answer = 0
    split_num = []
    start = 0
    for i in range(len(stations)):
        end = stations[i] - w - 1
        split_num.append(end-start)
        start = stations[i] + w
        if start > n: break
        if len(stations)-1 == i: split_num.append(n-start)
    for num in split_num:
        value, remainder = divmod(num,(w*2+1))
        if remainder: answer += (value+1)
        else: answer += value
    return answer