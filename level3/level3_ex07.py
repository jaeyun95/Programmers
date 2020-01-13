#(7) 단어변환

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
	
#다른 코드
'''
from collections import defaultdict

def nextWord(cur, words):
    ret = []
    for word in words:
        if sum([word[i] != cur[i] for i in range(len(word))]) == 1:
            ret.append(word)
    return ret

def bfs(begin, target, words):
    visited = defaultdict(lambda: False)
    queue = nextWord(begin, words)
    level = 0

    while(len(queue) > 0):
        size = len(queue)
        level += 1

        for _ in range(size):
            key = queue.pop(0)
            visited[key] = True
            if (key == target):
                return level
            for candidate in nextWord(key, words):
                if (visited[candidate] == False):
                    queue.append(candidate)

    return 0

def solution(begin, target, words):
    answer = bfs(begin, target, words)
    return answer
'''