def solution(a, b):
    sum = 0
    if a>b:
        tmp = a
        a = b
        b = tmp
    n = b - a + 1
    sum = n * (a + b) / 2
    return sum
print(solution(3,5))