#(34) 불량 사용자

import re
from itertools import combinations, permutations

def solution(user_id, banned_id):
    answer = []
    all_combination = list(permutations(user_id,len(banned_id)))
    banned_search_ids = []
    for i,b_id in enumerate(banned_id):
        search_id = ''
        for b_char in b_id:
            if '*' == b_char: search_id += '\w'
            else: search_id += b_char
        banned_search_ids.append(search_id)
    for i,banned_search_id in enumerate(banned_search_ids):
        compare = re.compile(banned_search_id)
        for user_id_combination in all_combination[:]:
            if (compare.match(user_id_combination[i])) and (len(banned_id[i])==len(user_id_combination[i])):
                continue
            all_combination.remove(user_id_combination)
    answer = [tuple(sorted(list(item))) for item in all_combination if sorted(list(item)) not in answer]
    answer = list(set(answer))
    return len(answer)
