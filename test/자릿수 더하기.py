def solution(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans

print(solution(100032))