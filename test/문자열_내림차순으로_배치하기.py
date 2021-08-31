def solution(s):
    arr = []
    ans = ""

    for char in s:
        arr.append(ord(char))
    
    arr.sort(reverse=True)
    
    for ascii in arr:
        ans += chr(ascii)
    
    return ans

print(solution("Zbcdefg"))