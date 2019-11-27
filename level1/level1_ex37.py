#(37) [1차]비밀지도

def solution(n, arr1, arr2):
    arr_bin = [ format(value1|value2, 'b').zfill(len(arr1)) for value1,value2 in zip(arr1,arr2)]
    return [ final.replace('1','#').replace('0',' ') for final in arr_bin ]