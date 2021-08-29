import numpy as np

def isint(num):
    if num - int(num) == 0:
        return True
    else:
        return False

def solution(n):
    r = np.sqrt(n)
    if isint(r):
        return (r + 1) ** 2
    else:
        return -1


