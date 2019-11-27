#(5) 스킬트리

def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_order = ""
        for alpha in skill_tree:
            if skill.find(alpha) != -1: skill_order += alpha
        if skill_order == skill[:len(skill_order)]: answer += 1
    return answer