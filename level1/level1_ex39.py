#(39) [1차]다트게임

bonus = ['S','D','T']
option = ['#','*']
def solution(dartResult):
    answer = 0
    value_list = []
    option_list = [1,1,1]
    bonus_list = []
    for i,char in enumerate(dartResult):
        if not char.isdigit():
            if char in bonus:
                bonus_list.append(bonus.index(char)+1)
            else:
                if char is '#': option_list[len(value_list)-1] *= -1
                else:
                    if len(value_list) == 1: option_list[0] *= 2
                    else:
                        option_list[len(value_list)-1] *= 2
                        option_list[len(value_list)-2] *= 2
        if char.isdigit():
            if i > 0 and dartResult[i-1].isdigit(): continue
            if dartResult[i+1].isdigit(): value_list.append(int(char+dartResult[i+1]))
            else: value_list.append(int(char))
    for i,value in enumerate(value_list):
        answer += pow(value,bonus_list[i])*option_list[i]
    return answer
	
	
# 다른 코드
'''
import re
def solution(dartResult):
    shot = re.findall(r'\d{1,2}[SDT][*#]?', dartResult)
    opt = [1,1,1]
    for i, s in enumerate(shot):
        if s[-1] == '#':
            opt[i] *= -1
            shot[i] = shot[i][:-1]
        elif s[-1] == '*':
            opt[i] *= 2
            shot[i] = shot[i][:-1]
            if i:
                opt[i-1] *= 2
    point = [(int(s[:-1]) ** '0SDT'.find(s[-1]) * o) for s, o in zip(shot, opt)]
    return sum(point)
'''