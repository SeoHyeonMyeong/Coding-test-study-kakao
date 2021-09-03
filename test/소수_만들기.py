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
    return arr

def delete_multi(n, arr):
    result = []
    for i in arr:
        if i == n or i % n != 0:
            result.append(i)
    return result

def solution(nums):
    prime_numbers = eratos(3000)
    n = len(nums)
    ans = 0
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i] + nums[j] + nums[k] in prime_numbers:
                    ans += 1
    return ans

nums=[1,2,7,6,4]
print(solution(nums))