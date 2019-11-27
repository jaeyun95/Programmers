#(13) H-Index

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        if citations[i] >= len(citations)-i: return len(citations)-i
    return 0
	

#다른 코드
'''
def solution(citations):
    for i in range(len(citations)-1,0,-1):
        c_list = [n for n in citations if n >= i+1]
        if i+1 <= len(c_list): return i+1
    return 0
'''