#(32) 타겟 넘버

def solution(numbers, target):
    answer_tree=[0]
    for number in numbers:
        node_list=[]
        for tree_number in answer_tree:
            node_list.append(tree_number+number)
            node_list.append(tree_number-number)
        answer_tree=node_list
    answer = answer_tree.count(target)
    return answer
	
#다른 코드
'''
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
'''