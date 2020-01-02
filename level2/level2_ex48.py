#(48) [3차]압축

def solution(msg):
    dic = dict()
    for index in range(26):
        dic[chr(65+index)] = index+1
    answer = []
    length = 0
    index = 0
    while True:
        length += 1
        if not msg[index:index+length] in dic:
            answer.append(dic[msg[index:index+length-1]])
            dic[msg[index:index+length]] = len(dic) + 1
            index += length -1
            length = 0
            continue
        if index + length-1 == len(msg):
            answer.append(dic[msg[index:index+length-1]])
            break
    return answer
	
#다른 코드
'''
def solution(msg):
    answer = []
    tmp = {chr(e + 64): e for e in range(1, 27)}
    num = 27
    while msg:
        tt = 1
        while msg[:tt] in tmp.keys() and tt <= msg.__len__():
            tt += 1
        tt -= 1
        if msg[:tt] in tmp.keys():
            answer.append(tmp[msg[:tt]])
            tmp[msg[:tt + 1]] = num
            num += 1
        msg = msg[tt:]
    return answer
'''