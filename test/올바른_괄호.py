def solution(s):
    stack = []
    for char in s:
        if char =='(':
            stack.append(1)
        elif char ==')':
            if len(stack)==0:
                return False
            stack.pop()
    if len(stack) ==0:
        return True
    return False

print(solution("(()("))