#(2) 모의고사

def solution(answers):
    # 패턴 정의
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 사람당 스코어 정의
    person1_ans = 0
    person2_ans = 0
    person3_ans = 0
    # 정답 확인
    for number in range(len(answers)):
        if answers[number] == person1[number%5]:
            person1_ans += 1
        if answers[number] == person2[number%8]:
            person2_ans += 1
        if answers[number] == person3[number%10]:
            person3_ans += 1
    pre_answer = [person1_ans, person2_ans, person3_ans]
    answer = []
    # 가장 많이 맞힌 사람 찾기
    for person, score in enumerate(pre_answer):
        if score == max(pre_answer):
            answer.append(person+1)
    return answer
	
	
# 다른 코드
'''
def solution(answers):
    # 패턴 정의
    person_ans = [[1, 2, 3, 4, 5],
              [2, 1, 2, 3, 2, 4, 2, 5],
              [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    # 스코어 리스트 정의
    score = [0]*len(person_ans)
    
    for number,ans in enumerate(answers):
        for index, person in enumerate(person_ans):
            if ans == person[number%len(person)]:
                score[index] += 1
    return [person + 1 for person, ans in enumerate(score) if ans == max(score)]
'''