#(9) 소수 찾기

from itertools import permutations
def search(n):
    n_list = set([num for num in range(3, n+1, 2)])
    for i in range(3, n+1, 2):
        if i in n_list:
            n_list -= set([i for i in range(i*2, n+1, i)])
    return n_list | set([2])

def solution(numbers):
    number_list = set([int("".join(item)) for i in range(7) for item in set(permutations(list(numbers), i + 1))])
    search_number_list = search(pow(10,len(numbers)))
    return len(number_list - (number_list - search_number_list))
	