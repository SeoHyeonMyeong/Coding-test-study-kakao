def solution(a, b):
    sum = 0
    for i in range(a,b+1):
        sum += i
    return sum
print(solution(3,5))