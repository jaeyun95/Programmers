#(34) 직사각형 별찍기

def rectangle(a, b):
    for i in range(b):
        print("*"*a)
		
# 다른 코드
'''
a, b = map(int, input().strip().split(' '))
rectangle(a,b)
'''