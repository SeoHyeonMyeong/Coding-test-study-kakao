def solution(n):
    arr = []
    ans = ""
    for i in str(n):
        arr.append(i)
    arr.sort(reverse=True)
    for i in arr:
        ans += i
    return int(ans)

print(solution(100032))