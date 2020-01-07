#(5) 네트워크

def dfs(computers, visited, start):
        record = [start]
        while record:
            j = record.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    record.append(i)
                    
def solution(n, computers):
    answer = 0
    visited = [0]*n
    start = 0
    while 0 in visited:
        if visited[start] ==0:
            dfs(computers, visited, start)
            answer +=1
        start+=1
    return answer

	
#다른 코드
'''
def solution(n, computers):
    networks = [{i} for i in range(n)]
    for computer1 in range(n):
        for computer2 in range(computer1+1,n):
            if computers[computer1][computer2] == 1:
                for pos,network in enumerate(networks):
                    if computer1 in network:position1 = pos
                    if computer2 in network:position2 = pos
                if position1 != position2:
                    new_network = networks[position1]|networks[position2]
                    networks.pop(max(position1,position2))
                    networks.pop(min(position1,position2))
                    networks.append(new_network)
    return len(networks)
'''