#(41) 키패드 누르기

dial_dict = {'1':(0,3),'2':(1,3),'3':(2,3),'4':(0,2),'5':(1,2),'6':(2,2),
             '7':(0,1),'8':(1,1),'9':(2,1),'*':(0,0),'0':(1,0),'#':(2,0)}
def solution(numbers, hand):
    answer = ""
    now_L = dial_dict['*']
    now_R = dial_dict['#']
    for n in numbers:
        if n in [1,4,7]:
            answer += "L"
            now_L = dial_dict[str(n)]
        elif n in [3,6,9]:
            answer += "R"
            now_R = dial_dict[str(n)]
        else:
            target = dial_dict[str(n)]
            dist_R = abs(now_R[0]-target[0])+abs(now_R[1]-target[1])
            dist_L = abs(now_L[0]-target[0])+abs(now_L[1]-target[1])
            if dist_R > dist_L: 
                answer += "L"
                now_L = dial_dict[str(n)]
            elif dist_R < dist_L: 
                answer += "R"
                now_R = dial_dict[str(n)]
            else:
                if hand == "right": 
                    answer +="R"
                    now_R = dial_dict[str(n)]
                else: 
                    answer += "L"
                    now_L = dial_dict[str(n)]
    return answer