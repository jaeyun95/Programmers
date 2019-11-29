#(22) 다음 큰 숫자

def solution(n):
    bin_n = format(n, 'b')
    one_count = str(bin_n).count('1')
    add = 1
    while True:
        compare_count = str(format(n+add, 'b')).count('1')
        if one_count == compare_count:return add + n
        add += 1

	
	
#다른 코드
'''
def solution(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
'''