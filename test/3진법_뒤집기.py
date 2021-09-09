def solution(n):
    ter_list = inv_ternary(n)
    ans = decimal(ter_list)
    return ans

def inv_ternary(decimal):
    ans = []
    while decimal > 0:
        ans.append(decimal % 3)
        decimal = int(decimal/3)
    return ans

def decimal(ternary):
    n = 1
    ans = 0
    while len(ternary) > 0:
        item = ternary.pop()
        ans += n * item
        n *= 3
    return ans


print(solution(45))