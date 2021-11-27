from collections import deque

arr = [0] * 100001
arr[0] = 1

def solution(n, money):
    for m in money:
        for i in range(1,n+1):
            if i - m >= 0:
                arr[i] += arr[i-m]
    return arr[0:n+1]
n = 5
m = [1,2,5]
print(solution(n,m))


