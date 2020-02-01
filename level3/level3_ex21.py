#(21) 가장 긴 팰린드롬

def solution(s):
    answer = 0
    for size in range(1,len(s) + 1):
        count = 0
        for index in range(len(s)):
            sub = s[index:index+size]
            if (index + size) > len(s): break
            if sub == sub[::-1]:
                count = size
                break
        if answer < count: answer = count
    return answer