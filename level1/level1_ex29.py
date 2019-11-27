#(29) 행렬의 덧셈

import numpy
def solution(arr1, arr2):
    return (numpy.array(arr1) + numpy.array(arr2)).tolist()
	
# 다른 코드
'''
def solution(arr1, arr2):
    return [[arr1[i][j] + arr2[i][j] for j in range(len(arr1[0]))] for i in range(len(arr1))]
'''