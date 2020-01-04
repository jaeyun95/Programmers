#(1) 타일 장식물

def solution(N):
    fibo = [1,1]
    for i in range(2,N):
        fibo.append(fibo[-1] + fibo[-2])
    return (fibo[-1]*2+fibo[-2])*2
	
