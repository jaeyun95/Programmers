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
	
#다른 코드
'''
def solution(tickets):
    def helper(tickets, route):
        if tickets == []:
            return route
        left = [i for i in range(len(tickets)) if tickets[i][0] == route[-1]]
        if left == []:
            return None
        left.sort(key = lambda i: tickets[i][1])

        for next in left:
            rest = helper(tickets[:next]+tickets[next+1:], route+[tickets[next][1]])
            if rest is not None:
                return rest
    return helper(tickets, ["ICN"])
'''