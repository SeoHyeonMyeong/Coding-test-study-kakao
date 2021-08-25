a, b = map(int, input().strip().split(' '))
print(a,b)
print()

def solution(x, n):
    answer = []
    for i in range(n):
        answer.append(x*(i+1))
    return answer


print(solution(a,b))