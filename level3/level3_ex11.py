#(11) 여행경로

def solution(tickets):
    information = {}
    for ticket in tickets:
        information[ticket[0]] = information.get(ticket[0],[]) + [ticket[1]]
    for infor in information:
        information[infor].sort()
    answer = []
    now = ["ICN"]
    while now:
        top = now[-1]
        if top not in information or not information[top]: answer.append(now.pop(0))
        else:
            now.append(information[top][0])
            information[top] = information[top][1:]
    return answer