def solution(array, commands):
    ans = []
    for c in commands:
        i,j,k = c
        arr = array[i-1:j]
        arr.sort()
        ans.append(arr[k-1])
    return ans
