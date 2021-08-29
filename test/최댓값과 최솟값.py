def max(arr):
    max_num = arr[0]
    for num in arr:
        if num >= max_num:
            max_num = num
    return max_num

def min(arr):
    min_num = arr[0]
    for num in arr:
        if num <= min_num:
            min_num = num
    return min_num

def solution(s):
    arr = s.split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    return str(min(arr)) + ' ' + str(max(arr))

print(solution("-4 -2 -3 -4"))
