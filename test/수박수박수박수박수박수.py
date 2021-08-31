def solution(n):
    word = "수박"
    ans = word * int(n/2)
    if n%2 ==1:
        ans += "수"
    return ans

print(solution(8))