#(27) 예산

def solution(budgets, M):
    left, right, answer = 0, max(budgets), 0
    while(left<=right):
        mid = (left + right)//2
        all_budget = 0
        for budget in budgets:
            if budget < mid: all_budget += budget
            else: all_budget += mid
        if all_budget > M: right = mid -1
        else: 
            answer = mid
            left = mid + 1
    return answer