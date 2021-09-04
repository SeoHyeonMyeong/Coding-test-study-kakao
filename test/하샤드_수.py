def unit_sum(x):
    if x == 0:
        return 0
    else:
        return int(x%10) + unit_sum(x/10)

def solution(x):
    answer = x % unit_sum(x) == 0
    return answer

print(solution(10))