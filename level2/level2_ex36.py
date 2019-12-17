#(36) [3차] 파일명 정렬

import re
def solution(files):
    file_name = [re.split("([0-9]+)",file) for file in files]
    file_name.sort(key = lambda x: (x[0].lower(), int(x[1])))
    return ["".join(name) for name in file_name]
