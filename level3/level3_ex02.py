#(2) 정수 삼각형

def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(i+1):
            if j == 0: triangle[i][j] += triangle[i-1][j]
            elif j == i: triangle[i][j] += triangle[i-1][j-1]
            else: triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j-1])
    return max(triangle[-1])
	
#다른 코드
'''
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
'''