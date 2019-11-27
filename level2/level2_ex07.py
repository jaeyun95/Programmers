#(7) 탑

def solution(heights):
    answer = []
    for i in range(len(heights)-1,-1,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer.append(j+1)
                break
        if len(answer) != (len(heights)-i): answer.append(0)
    answer.reverse()
    return answer
	
	
#다른 코드
'''
def solution(heights):
    answer = [0]*len(heights)
    for i in range(len(heights)-1,0,-1):
        for j in range(i-1,-1,-1):
            if heights[i] < heights[j]:
                answer[i] = j+1
                break
    return answer
'''