#(23) 가장 먼 노드

from collections import defaultdict
def solution(n, edge):
    vertex_visit = [0]*n
    edge_list = defaultdict(list)
    for e in edge:
        edge_list[e[0]-1].append(e[1]-1)
        edge_list[e[1]-1].append(e[0]-1)
    check_list = [0]
    dist = 0
    while check_list:
        dist += 1
        size = len(check_list)
        for num in range(size):
            node = check_list.pop(0)
            if not vertex_visit[node]:
                vertex_visit[node] = dist
                check_list += edge_list[node]
    return vertex_visit.count(dist-1)