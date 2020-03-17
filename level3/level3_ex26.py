#(26) 입국심사

def solution(n, times):
    left, right, answer = 0, max(times)*n, 0
    while(right >= left):
        mid = (right + left)//2
        check = 0
        for time in times:
            check += mid//time
        if check >= n:
            answer = mid
            right = mid - 1
        else: left = mid + 1
    return answer