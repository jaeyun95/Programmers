#(34) 불량 사용자

import re
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    all_combination = list(permutations(user_id,len(banned_id)))
    banned_search_ids = []
    for i,b_id in enumerate(banned_id):
        search_id = '^{}$'.format(b_id.replace('*', '.'))
        banned_search_ids.append(search_id)
    for i,banned_search_id in enumerate(banned_search_ids):
        compare = re.compile(banned_search_id)
        for user_id_combination in all_combination[:]:
            if (compare.match(user_id_combination[i])):continue
            all_combination.remove(user_id_combination)
    answer = [tuple(sorted(list(item))) for item in all_combination if sorted(list(item)) not in answer]
    answer = list(set(answer))
    return len(answer)
	
#다른 코드
'''
def combi(temp, number, calculate):
    global result
    if len(temp) == len(calculate):
        temp = set(temp)
        if temp not in result:
            result.append(temp)
        return
    else:
        for j in range(len(calculate[number])):
            if calculate[number][j] not in temp:
                temp.append(calculate[number][j])
                combi(temp, number+1, calculate)
                temp.pop()
result = []
def solution(user_id, banned_id):
    global result
    calculate = []
    for ban in banned_id:
        possible=[]
        for user in user_id:
            if len(ban) != len(user):
                continue
            else:
                count = 0
                for i in range(len(ban)):
                    if user[i] == ban[i]:
                        count+=1
                if count == len(ban)-ban.count('*'):
                    possible.append(user)
        calculate.append(possible)

    combi([], 0, calculate)
    return len(result)
'''
