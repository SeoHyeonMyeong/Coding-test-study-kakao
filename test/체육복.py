
def find_greedy(person,n):
    ans = -1
    for i in range(n):
        me = person[i]
        if i == 0:
            left = 0
        else:
            left = person[i-1]
        
        if i == n-1:
            right = 0
        else:
            right = person[i+1]

        condition = me == 0
        condition_1 = left == 2 and right != 2
        condition_2 = right == 2 and left != 2
        condition_3 = left == 2 and right == 2
        if condition:
            if condition_1:
                return i, -1
            elif condition_2:
                return i, +1
            elif condition_3:
                ans = i
    return ans, -1

def solution(n, lost, reserve):
    person = [1] * n
    for i in reserve:
        person[i-1] += 1
    for i in lost:
        person[i-1] -= 1 

    greedy, direction = find_greedy(person,n)
    while greedy != -1:
        person[greedy] += 1
        person[greedy + direction] -= 1
        greedy,direction = find_greedy(person,n)
    
    result = 0
    for i in person:
        if i != 0:
            result += 1
    return result
    




n = 12
lost = [1,2,3,4,8,9,10,11]
reserve = [9,10]

print(solution(n,lost,reserve))