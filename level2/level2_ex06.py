#(6) 다리를 지나는 트럭

def solution(bridge_length, weight, truck_weights):
    bridge = [0]*bridge_length
    answer = 0
    while bridge:
        answer+= 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight: 
                bridge.append(truck_weights.pop(0))
            else: 
                bridge.append(0)
    return answer
	
# 테스트 5에서 시간초과가 뜹니다! 조만간 업데이트 하겠습니다 -2019/11/28