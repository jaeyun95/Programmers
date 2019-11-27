#(35) 예산

def solution(d, budget):
    d.sort()
    total_buy = []
    for i in d:
        total_buy.append(i)
        if sum(total_buy) > budget:
            total_buy = total_buy[:-1]
            break
    return len(total_buy)
		
# 다른 코드
'''
def solution(d, budget):
    d.sort()
    total_buy = 0
    for i in d:
        if i <= budget:
            budget -= i
            total_buy += 1
    return total_buy
'''