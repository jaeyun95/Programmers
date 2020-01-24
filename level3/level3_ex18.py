#(18) 숫자 게임

def solution(A, B):
    answer = 0
    if min(A) > max(B): return 0
    B.sort()
    A.sort()
    for a in A:
        for b in B:
            if b-a > 0:
                answer += 1
                B.remove(b)
                break
    return answer