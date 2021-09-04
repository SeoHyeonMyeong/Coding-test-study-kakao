def solution(n):
    ans = []
    for i in str(n):
        ans.append(int(i))
    return ans[::-1]

print(solution(100032))