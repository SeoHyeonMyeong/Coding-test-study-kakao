from collections import deque

def solution(s):
    n = len(s)
    s = deque(s)

    ans = 0
    for i in range(n):
        stack = deque()
        for i in range(n):
            item = s[i]
            if item in ['(','{','[']:
                stack.append(item)
            if item in [')','}',']']:
                if len(stack) == 0:
                    break
                a = {')':'(','}':'{',']':'['}.get(item)
                b = stack.pop()
                if a != b:
                    break
            if i == n-1 and len(stack) == 0:
                ans +=1
        s.rotate(1)
    return ans

# s = "[]{}()"
# print(solution(s))