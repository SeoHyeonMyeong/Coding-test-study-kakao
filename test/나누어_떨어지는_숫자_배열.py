def solution(arr, divisor):
    result = []
    for i in arr:
        if i % divisor == 0:
            result.append(i)
    if len(result)==0:
        return [-1]
    result.sort()
    return result

print(solution([2,36,1,3],1))