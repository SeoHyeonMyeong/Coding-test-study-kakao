
def solution(bridge_length, weight, truck_weights):
    queue = [0] * bridge_length
    
    time = 0 
    while len(truck_weights) != 0:
        print(queue)
        time += 1
        queue.pop(0)
        if sum(queue) + truck_weights[0] <= weight:
            queue.append(truck_weights.pop(0))
        else:
            queue.append(0)
    return time + bridge_length


bridge = 2
weight = 10
truck = [7,4,5,6]

print(solution(bridge, weight, truck))