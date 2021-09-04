import numpy as np

array1 = [[1,2],[2,3]]
array2 = [[1,2],[2,3]]

def solution(arr1, arr2):
    answer = np.array(arr1) + np.array(arr2)
    answer = answer.tolist()
    print(answer)
    return answer

solution(array1,array2)