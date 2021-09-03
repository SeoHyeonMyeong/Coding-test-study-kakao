# 3진법

def solution(n):
    ans = ""
    while n != 0:
        n -= 1
        if n % 3 == 0:
            ans = "1" + ans
        elif n % 3 == 1:
            ans = "2" + ans
        elif n % 3 == 2:
            ans = "4" + ans
        n = int(n/3)
    return ans

print(solution(10))




