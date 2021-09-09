import numpy as np

def solution(left, right):
    ans = 0
    for num in range(left, right+1):
        root = np.sqrt(num)
        if root - int(root) == 0:
            ans -= num
        else:
            ans += num
    return ans

print(solution(24,27))