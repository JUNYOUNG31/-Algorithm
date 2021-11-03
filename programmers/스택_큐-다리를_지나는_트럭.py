# 다리를 지나는 트럭

# 트럭 여러 대가 강을 가로지르는 일차선 다리를 정해진 순으로 건너려 합니다. 모든 트럭이 다리를 건너려면 최소 몇 초가
# 걸리는지 알아내야 합니다. 다리에는 트럭이 최대 bridge_length대 올라갈 수 있으며, 다리는 weight 이하까지의 무게를
# 견딜 수 있습니다. 단, 다리에 완전히 오르지 않은 트럭의 무게는 무시합니다.
# 예를 들어, 트럭 2대가 올라갈 수 있고 무게를 10kg까지 견디는 다리가 있습니다. 무게가 [7, 4, 5, 6]kg인 트럭이 순서대로
# 최단 시간 안에 다리를 건너려면 다음과 같이 건너야 합니다.

def solution(bridge_length, weight, truck_weights):
    answer = 0
    on_bridge = [0] * bridge_length
    while on_bridge:
        answer += 1
        on_bridge.pop(0)
        if truck_weights:
            if sum(on_bridge) + truck_weights[0] <= weight:
                on_bridge.append(truck_weights.pop(0))
            else:
                on_bridge.append(0)
    return answer





# 실패작
# def solution(bridge_length, weight, truck_weights):
#     answer = 0
#     on_bridge = []
#     time = 0
#     stop = len(truck_weights)
#     cnt = 0
#     while cnt != stop:
#         if len(truck_weights) != 0 and sum(on_bridge) + truck_weights[0] <= weight:
#             on_bridge.append(truck_weights.pop(0))
#         time += 1
#         print(truck_weights)
#         print(on_bridge)
#         print(time)
#         if time == bridge_length:
#             on_bridge.pop(0)
#             time = 0
#             cnt += 1
#         answer += 1
#         print(answer)
#     # while on_bridge:
#     #     on_bridge.pop(0)
#     #     answer += 1
#     return answer


# bridge_length = 2
bridge_length = 100
# weight = 10
weight = 100
# truck_weights = [7,4,5,6]
truck_weights = [10,10,10,10,10,10,10,10,10,10]
print(solution(bridge_length, weight, truck_weights))