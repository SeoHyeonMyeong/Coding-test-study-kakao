def solution(A,B):
    
    A.sort()
    B.sort(reverse=True)
    sum = 0

    for i in range(len(A)):
        sum += A[i] * B[i]
    return sum

a = [1,4,2]
b = [5,4,4]
print(solution(a,b))