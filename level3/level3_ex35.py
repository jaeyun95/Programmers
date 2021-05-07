#(35) 보석 쇼핑

def solution(gems):
    size = len(set(gems))
    category = {gems[0]:1}
    left, right = 0, 0
    answer = [0,len(gems)-1]
    while (left < len(gems)) and (right < len(gems)):
        if size == len(category):
            if (right - left) < (answer[1]-answer[0]):
                answer = [left,right]
            if category[gems[left]] == 1:
                del category[gems[left]]
            else:
                category[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if right == len(gems): break
            else: category[gems[right]] = category.get(gems[right],0) + 1
    return [answer[0]+1, answer[1]+1]


    