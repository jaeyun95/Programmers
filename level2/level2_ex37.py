#(37) [1차]뉴스 클러스터링

from collections import Counter
def solution(str1, str2):
    str1_list = [str1[index].lower()+str1[index+1].lower() for index in range(len(str1)-1) if str1[index].isalpha() and str1[index+1].isalpha()]
    str2_list = [str2[index].lower()+str2[index+1].lower() for index in range(len(str2)-1) if str2[index].isalpha() and str2[index+1].isalpha()]
    str1_set = Counter(str1_list)
    str2_set = Counter(str2_list)
    intersection = len(list((str1_set&str2_set).elements()))
    union = len(list((str1_set|str2_set).elements()))
    if union == 0: return 65536
    return int(intersection/union*65536)
	
#다른 코드
'''
from collections import Counter
import re
def solution(str1, str2):
    str1_list = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2_list = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    str1_set = Counter(str1_list)
    str2_set = Counter(str2_list)
    intersection = len(list((str1_set&str2_set).elements()))
    union = len(list((str1_set|str2_set).elements()))
    if union == 0: return 65536
    return int(intersection/union*65536)
'''
