def solution(s, n):
    ans = ""
    alphaNum = ord('z') - ord('a') + 1
    for char in s:
        ascii = ord(char)
        if ascii == ord(' '):
            ans += ' '
        elif ascii >= ord('a') and ascii <= ord('z'):
            ascii += n
            if ascii > ord('z'):
                ascii -= alphaNum
            ans += chr(ascii)
        elif ascii >= ord('A') and ascii <= ord('Z'):
            ascii += n
            if ascii > ord('Z'):
                ascii -= alphaNum
            ans += chr(ascii)
    return ans

print(solution("abcdE ZYX",2))