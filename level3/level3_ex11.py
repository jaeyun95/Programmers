#(11) 여행경로

def solution(tickets):
    information = {}
    for ticket in tickets:
        information[ticket[0]] = information.get(ticket[0],[]) + [ticket[1]]
    for infor in information:
        information[infor].sort(reverse=True)
    answer = []
    now = ["ICN"]
    while now:
        top = now[-1]
        if top not in information or not information[top]: answer.append(now.pop())
        else:
            now.append(information[top][-1])
            information[top] = information[top][:-1]
    return answer[::-1]