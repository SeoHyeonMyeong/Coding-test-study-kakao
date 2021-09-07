open_set = []

def solution(numbers, target):
    # init
    open_set.append([numbers[0],[True]])
    open_set.append([-numbers[0],[False]])
    
    limit = sum([i for i in numbers])
    limit_depth = len(numbers)

    ans = 0

    while len(open_set) != 0:
        set = open_set.pop()
        temp = set[0]
        signs = set[1]
        depth = len(set[1])
        if depth == limit_depth:
            if temp == target:
                ans += 1
        else:
            # plus
            last_sum = 0
            for i in range(depth,limit_depth):
                last_sum += numbers[i]
            if abs(target-temp) <= last_sum:
                #plus
                new_temp = temp + numbers[depth]
                new_signs = signs.copy()
                new_signs.append(True)
                open_set.append([new_temp,new_signs])

                #minus
                new_temp = temp - numbers[depth]
                new_signs = signs.copy()
                new_signs.append(False)
                open_set.append([new_temp,new_signs])
    return ans

nums = [1, 1, 1, 1, 1]
target = 3

print(solution(nums, target))
