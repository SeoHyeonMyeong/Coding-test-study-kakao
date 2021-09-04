import numpy as np

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

def solution(arr1, arr2):
    answer = np.array(arr1).dot(np.array(arr2))
    answer = answer.tolist()
    print(answer)
    return answer

solution(arr1,arr2)