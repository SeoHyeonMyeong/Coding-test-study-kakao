from collections import deque

def solution(s):
    s = deque(s)
    iteration = 0
    count_zero = 0
    while len(s) != 1:
        iteration += 1
        n = len(s)
        for i in range(n):
            item = s.pop()
            if item == "1":
                s.appendleft(item)
            else:
                count_zero += 1
        s = len_to_binary(len(s))
        s = deque(s)
    return [iteration, count_zero]


def len_to_binary(n):
    ans = ""
    if n == 0:
        return "0"
    while n != 1:
        if n % 2 == 0:
            ans = "0" + ans
        else:
            ans = "1" + ans
        n = int(n/2)
    ans = "1" + ans
    return ans

s = "101010"
print(solution(s))