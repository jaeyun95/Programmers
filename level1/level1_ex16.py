#(16) 소수 찾기

def solution(n):
    n_list = set([num for num in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in n_list:
            n_list -= set([i for i in range(i*2, n+1, i)])
    return len(n_list) + 1