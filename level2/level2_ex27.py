#(27) 오픈채팅방

def solution(record):
    user_info = {}
    answer = []
    for i,sentence in enumerate(record):
        information = sentence.split(' ')
        answer.append(information)
        if not(information[1] in user_info):  user_info[information[1]] = information[2]
        if information[0] == "Enter": user_info[information[1]] = information[2]
        elif information[0] == "Change": 
            user_info[information[1]] = information[2]
            answer.pop()
    for i,sentence in enumerate(answer):
        if sentence[0] == 'Enter': answer[i] = "{}님이 들어왔습니다.".format(user_info[sentence[1]])
        else: answer[i] = "{}님이 나갔습니다.".format(user_info[sentence[1]])
    return answer
	
	
#다른 코드
'''
def solution(record):
    answer = []
    namespace = {}
    printer = {'Enter':'님이 들어왔습니다.', 'Leave':'님이 나갔습니다.'}
    for r in record:
        rr = r.split(' ')
        if rr[0] in ['Enter', 'Change']:
            namespace[rr[1]] = rr[2]

    for r in record:
        if r.split(' ')[0] != 'Change':
            answer.append(namespace[r.split(' ')[1]] + printer[r.split(' ')[0]])

    return answer
'''