#(10) 2016년

week = ["THU","FRI","SAT","SUN","MON","TUE","WED"]
date = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]

def solution(a, b):
    return week[(sum(date[:a-1]) + b)%7]
	
	
# 다른 코드
'''
import datetime

week = ["MON","TUE","WED","THU","FRI","SAT","SUN",]

def solution(a, b):
    return week[datetime.date(2016,a,b).weekday()]
'''