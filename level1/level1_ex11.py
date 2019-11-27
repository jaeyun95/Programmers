#(11) 체육복

def solution(n, lost, reserve):
    # 실제로 reserve와 lost의 리스트를 구함
    real_reserve = [ p for p in reserve if p not in lost]
    real_lost = [ p for p in lost if p not in reserve]
    answer = n - len(real_lost)
    for student in real_lost:
        if student-1 in real_reserve:
            real_reserve.remove(student-1)
            answer += 1
        elif student+1 in real_reserve:
            real_reserve.remove(student+1)
            answer += 1
    return answer
	
	
# 다른 코드
'''
def solution(n, lost, reserve):
    # 실제로 reserve와 lost의 리스트를 구함
    real_reserve = [ p for p in reserve if p not in lost]
    real_lost = [ p for p in lost if p not in reserve]
    for student in real_reserve:
        if student-1 in real_lost:
            real_lost.remove(student-1)
        elif student+1 in real_lost:
            real_lost.remove(student+1)
    return n - len(real_lost)
	
	or
	
def solution(n, lost, reserve):
    # 실제로 reserve와 lost의 리스트를 구함
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    for student in real_reserve:
        if student-1 in real_lost:
            real_lost.remove(student-1)
        elif student+1 in real_lost:
            real_lost.remove(student+1)
    return n - len(real_lost)
'''