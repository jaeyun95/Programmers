#(7) 단어 변환

def solution(begin,target,words):
    if target not in words:
        return 0
    level = [begin]
    answer = 0
    while(len(words)!=0):
        answer += 1
        for level_word in level:
            pre_level = []
            for word in words:
                count=0
                for a, b in zip(level_word, word):
                    if a != b: count += 1
                if count==1:
                    pre_level.append(word)
                    words.remove(word)
        if target in pre_level:
            return answer
        level = pre_level
    return 0