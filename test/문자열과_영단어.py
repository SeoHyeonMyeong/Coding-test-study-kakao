code = ["zero","one","two","three","four","five","six","seven","eight","nine"]


def solution(s):
    temp = ""
    ans = ""
    for char in s:
        if char.isnumeric():
            ans += char
        else:
            temp += char
            if temp in code:
                ans += str(code.index(temp))
                temp = ""
    return int(ans)

print(solution("one4seveneight"))