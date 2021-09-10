import numpy as np

object = []


def solution(n, computers):
    global object
    object = np.zeros(n)
    ans = 0
    for i in range(n):
        if object[i] == 1:
            pass
        else:
            search(i,computers)
            ans +=1
    return ans

def search(n,computers):
    global object
    object[n] = 1
    li = object - computers[n]
    for i in range(len(li)):
        if li[i] == -1:
            search(i,computers)
    

# n = 5
# computers = [
#     [1, 1, 0, 0, 0],
#     [1, 1, 0, 0, 0],
#     [0, 0, 1, 0, 0],
#     [0, 0, 0, 1, 0],
#     [0, 0, 0, 0, 1]
# ]

n = 4
computers = [
    [1,1,0,1],
    [1,1,0,0],
    [0,0,1,1],
    [1,0,1,1]
]
print(solution(n,computers))

# A = np.array([1,1,0])
# B = np.array([1,0,1])
# print(-1 in (A - B))