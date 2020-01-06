#(4) 하노이의 탑

def hanoi(num, start, to, mid, answer):
    if num == 1:
        return answer.append([start, to])
    hanoi(num-1, start, mid, to, answer)
    answer.append([start, to])
    hanoi(num-1, mid, to, start, answer)
    
def solution(n):
    answer = []
    hanoi(n, 1, 3, 2, answer)
    return answer
	
#다른 코드
'''
## first
def hanoi(n):

    def _hanoi(m, s, b, d):
        if m == 1:
            yield [s, d]
        else:
            yield from _hanoi(m-1, s, d, b)
            yield [s, d]
            yield from _hanoi(m-1, b, s, d)

    ans = list(_hanoi(n, 1, 2, 3))
    return ans

	
## second
def move_n_disk(n, i, f):
    if n==1: return [[i, f]]
    return move_n_disk(n-1, i, 6-i-f) + move_n_disk(1, i, f) + move_n_disk(n-1, 6-i-f, f)

def hanoi(n):
    answer = move_n_disk(n, 1, 3)
    return answer
'''