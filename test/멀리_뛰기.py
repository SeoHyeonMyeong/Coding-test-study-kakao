def solution(n):
    if n<=1:
        return 1
    arr = []
    arr.append(1)
    arr.append(1)
    for i in range(2,n+1):
        arr.append(arr[i-1] + arr[i-2])
    return arr[n]

print(solution(6))