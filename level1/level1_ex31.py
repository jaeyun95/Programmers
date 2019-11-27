#(31) 콜라츠 추측

def collatz(num, iteration):
    if iteration > 500: return -1
    if num == 1: return iteration
    if num % 2 == 0: num = num//2
    else: num = num*3 + 1
    iteration += 1
    return collatz(num, iteration)

def solution(num):
    return collatz(num, 0)
	
# 다른 코드
'''
def solution(num):
    iteration = 0
    while num > 1:
        num = num * 3 + 1 if num%2 else num/2
        iteration += 1
    return iteration if iteration < 500 else -1
'''