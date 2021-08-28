def avarage(arr):
    n = 0
    sum = 0
    for num in arr:
        n += 1
        sum += num
    return sum/n

def solution(arr):
    answer = avarage(arr)
    return answer