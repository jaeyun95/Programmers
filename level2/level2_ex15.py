#(15) 큰 수 만들기 

def solution(number, k):
    len_number = len(number)
    start = 0
    for count in range(k):
        for index in range(start, len_number-1):
            if number[index] < number[index+1]:
                number = number[:index] + number[index+1:]
                len_number -= 1
                if index > 0: start = index-1
                break
        else:
            number = number[:len_number-k+count]
            break
    return "".join(list(map(str,number)))
