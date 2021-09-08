def solution(p):
    if p == "":
        return ""
    open = 0
    close = 0
    i = 0
    while open != close or i == 0:
        if p[i] == "(":
            open += 1
        elif p[i] == ")":
            close += 1
        i += 1
    u = p[:i]
    v = p[i:]

    print([u,v])
    if is_perfact(u):
        if v =="":
            return u
        return u + solution(v)
    else:
        temp = "(" + solution(v) + ")"
        if len(u)>2:
            temp += reverse(u[1:-1])
        return temp
    
def is_perfact(p):
    stack = []
    for char in p:
        if char == "(":
            stack.append(1)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    if len(stack) == 0:
        return True
    return False

def reverse(p):
    temp = ""
    for char in p:
        if char == "(":
            temp += ")"
        elif char == ")":
            temp += "("
    return temp

# print(solution("()))((()"))