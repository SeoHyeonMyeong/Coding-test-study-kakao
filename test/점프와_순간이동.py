def solution(n):
    ans = 0
    binary = format(n,'b')
    ans = sum(int(i) for i in binary)
    return ans

n = 5000
print(solution(n))