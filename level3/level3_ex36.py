#(36) 합승 택시 요금


### dijkstra
import heapq

def dijkstra(start, graph):
    distance = {key: float("INF") for key in range(1, len(graph))}
    heap = []
    distance[start] = 0
    heapq.heappush(heap, [distance[start], start])
    while heap:
        now_dis, now_node = heapq.heappop(heap)
        for next_node, next_dis in graph[now_node]:
            if distance[next_node] > (next_dis + now_dis):
                distance[next_node] = next_dis + now_dis
                heapq.heappush(heap, [distance[next_node], next_node])
    return distance

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for fare in fares:
        graph[fare[0]].append([fare[1], fare[2]])
        graph[fare[1]].append([fare[0], fare[2]])
    distance = dijkstra(s,graph)
    cost = float("INF")
    for k in range(1,n+1):
        distance_k = dijkstra(k,graph)
        cost = min(cost,distance[k]+distance_k[a]+distance_k[b])
    return cost

### floyd
def solution(n, s, a, b, fares):
    distance = [[float("INF") for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j: distance[i][j] = 0

    for fare in fares:
        distance[fare[0]][fare[1]] = fare[2]
        distance[fare[1]][fare[0]] = fare[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    cost = float("INF")
    for k in range(1, n + 1):
        cost = min(cost, distance[s][k] + distance[k][a] + distance[k][b])
    return cost
