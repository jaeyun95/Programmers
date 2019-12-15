#(35) 영어 끝말잇기

def solution(n, words):
    turn = 0
    stage = 0
    mention = []
    for index, word in enumerate(words):
        if (index+1)%n == 1: 
            turn = 1
            stage += 1
        if word in mention: return [turn,stage]
        if mention:
            if mention[index-1][-1] != word[0]: return [turn,stage]
        turn += 1
        mention.append(word)
    return [0,0]
	
#다른 코드
'''
def solution(n, words):
    for p in range(1, len(words)):
        if words[p][0] != words[p-1][-1] or words[p] in words[:p]: return [(p%n)+1, (p//n)+1]
    else:
        return [0,0]
'''
