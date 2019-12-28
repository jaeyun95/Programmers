#(42) 숫자 야구

from itertools import permutations
def solution(baseball):
    all_list = list(permutations([1,2,3,4,5,6,7,8,9],3))
    for item in all_list[:]:
        for baseball_item in baseball:
            baseball_num = [int(i) for i in list(str(baseball_item[0]))]
            strike = 0
            for index in range(len(baseball_num)):
                if baseball_num[index] == item[index]: strike += 1
            if baseball_item[1] != strike: 
                all_list.remove(item)
                break
            ball = len(set(baseball_num)&set(item)) - strike
            if ball != baseball_item[2]:
                all_list.remove(item)
                break
    return len(all_list)