def solution(n, s):
    if n > s:
        return [-1]
    a = s // n
    b = s % n
    ans = [a] * (n-b) + [a+1] * b 
    return ans

n = 3
s = 10
print(solution(n,s))