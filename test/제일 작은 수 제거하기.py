def solution(arr):
    if len(arr) == 1:
        return [-1]
    else:
        min = arr[0]
        min_index = 0
        for i in range(len(arr)):
            if arr[i] < min:
                min = arr[i]
                min_index = i
        arr.pop(min_index)
        return arr
    