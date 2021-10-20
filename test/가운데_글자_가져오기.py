def solution(s):
    l = len(s)
    mid = int(l/2)
    if l % 2 == 0:
        return s[mid-1:mid+1]
    return s[mid]

print(solution("abcd"))