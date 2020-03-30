#(32) 배달

import math
def solution(N, road, K):
    distance = [math.inf for _ in range(N)]
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    for start, end, weight in road:
        start -= 1
        end -= 1
        if matrix[start][end] == 0 and matrix[end][start] == 0:
            matrix[start][end], matrix[end][start] = weight, weight
        else:
            if weight < matrix[start][end]:
                matrix[start][end], matrix[end][start] = weight, weight

    queue = [0]
    distance[0] = 0
    while queue:
        y = queue.pop()
        for x in range(N):
            if matrix[y][x] != 0:
                if distance[x] > distance[y] + matrix[y][x] and distance[y] + matrix[y][x] <= K:
                    distance[x] = distance[y] + matrix[y][x]
                    queue.append(x)
    return len([i for i in distance if i <= K])