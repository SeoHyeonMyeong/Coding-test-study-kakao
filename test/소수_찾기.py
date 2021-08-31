import numpy as np

def eratos(n):
    arr = []
    count = 0
    limit = int(np.sqrt(n)+1)
    for i in range(2,n+1):
        arr.append(i)
    while arr[count] < limit:
        arr = delete_multi(arr[count],arr)
        count += 1
    return len(arr)

def delete_multi(n, arr):
    result = []
    for i in arr:
        if i == n or i % n != 0:
            result.append(i)
    return result

def solution(n):
    return eratos(n)

print(eratos(10))