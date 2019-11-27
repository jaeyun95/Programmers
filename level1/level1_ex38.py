#(38) 문자열 압축

def solution(s):
    if len(s) == 1 : return len(s)
    for size in range(1,len(s)//2 + 1):
        count = 0
        pre_string= ""
        for i in range(0,len(s) + 1,size):
            if pre_string[-size:] == s[i:i+size]: count += 1
            else:
                if count > 1: pre_string += str(count) + s[i:i+size]
                else: pre_string += s[i:i+size]
                count = 1
        if size == 1: min_size = len(pre_string)
        else : 
            if min_size > len(pre_string):
                min_size = len(pre_string)
    return min_size