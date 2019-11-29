#(20) 행렬의 곱셈

import numpy as np
def solution(arr1, arr2):
    arr1_np = np.array(arr1)
    arr2_np = np.array(arr2)
    answer = np.matmul(arr1_np,arr2_np)
    return answer.tolist()
	
	
#다른 코드
'''
def solution(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]
'''