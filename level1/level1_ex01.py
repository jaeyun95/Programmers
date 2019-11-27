#(1) 완주하지 못한 선수

def solution(participant, completion):
    # sort를 사용하여 순서를 맞춤 같은 위치에 같은 이름이 아닌 경우
    # -->  participant부분에 있는 사람이 완주자가 아님
    participant.sort()
    completion.sort()
    # 두 리스트를 비교 후 다르다면 participant쪽의 값 리턴
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[-1]
	
	
# 다른 코드
'''
import collections

def solution(participant, completion):
    # collection모듈을 사용한 풀이
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
'''