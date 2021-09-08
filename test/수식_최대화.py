preference = [
    ["+","-","*"],
    ["+","*","-"],
    ["-","+","*"],
    ["-","*","+"],
    ["*","+","-"],
    ["*","-","+"]
]

def solution(expression):
    num, op = devide(expression)
    ans = 0
    for p in preference:
        value = calc(p,num.copy(),op.copy())
        if value > ans:
            ans = value
    return ans

def devide(expression):
    num = []
    op = []
    temp = ""
    for char in expression:
        if char.isnumeric():
            temp += char
        else:
            num.append(int(temp))
            temp = ""
            op.append(char)
    num.append(int(temp))
    return num,op

def calc(p, num, op):
    for ch in p:
        while ch in op:
            i = op.index(ch)
            if ch =="*":
                num[i] = num[i] * num.pop(i+1)
            if ch =="+":
                num[i] = num[i] + num.pop(i+1)
            if ch =="-":
                num[i] = num[i] - num.pop(i+1)
            op.pop(i)
    print([num,op])
    return abs(num[0])

ex = "100-200*300-500+20"
print(solution(ex))