#(47) 괄호 변환

def trans_number(n,number):
    num_list = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    answer = ''
    if number == 0: return '0'
    while number > 0:
        answer = num_list[number%n] + answer
        number = number//n
    return answer
def solution(n, t, m, p):
    all_number = ''
    answer = ''
    if p == m: p = 0
    for number in range(m*t):
        all_number += trans_number(n,number)
        if len(all_number) >= m*t: break
    for index,number in enumerate(all_number):
        if (index+1)%m == p: answer+= number
    return answer[:t]
	
#다른 코드
'''
big = ["A","B","C","D","E","F"]
def solution(n, t, m, p):
    a="0"
    i=0
    while True:
        if len(a)>=t*m:
            break
        b=""
        j=i
        while (j):
            if j%n>9:
                b=big[j%n-10]+b
            else:
                b=str(j%n)+b
            j=j//n
        a=a+b
        i=i+1
    answer = a[p-1::m][:t]
    return answer
'''