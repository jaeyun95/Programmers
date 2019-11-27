#(16) 구명보트

def solution(people, limit):
    people.sort()
    end_index = len(people)-1
    start_index = 0
    couple = 0
    while(start_index<end_index):
        if people[start_index] + people[end_index] <= limit:
            start_index += 1
            end_index -= 1
            couple += 1
        else: end_index -= 1
    return len(people)-couple