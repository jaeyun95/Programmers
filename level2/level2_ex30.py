#(30) N개의 최소공배수

from fractions import gcd
def solution(arr):
    answer = arr[0]
    for number in arr[1:]:
        answer = (answer*number)/gcd(answer,number)
    return answer