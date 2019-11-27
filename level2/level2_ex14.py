#(14) 위장

from collections import Counter
def solution(clothes):
    count_clothes = Counter([clo for _,clo in clothes])
    answer = 1
    for key in count_clothes:
        answer *= (count_clothes[key]+1)
    return answer - 1