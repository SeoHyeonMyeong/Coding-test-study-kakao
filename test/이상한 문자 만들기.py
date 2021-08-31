def solution(s):
    arr = s.split(' ')
    print(arr)
    ans = ''
    for str in arr:
        switch = False
        for char in str:
            if switch:
                ans += char.lower()
            else:
                ans += char.upper()
            switch = not switch
        ans += ' '
    print(ans)
    return ans

solution("hello world its me")