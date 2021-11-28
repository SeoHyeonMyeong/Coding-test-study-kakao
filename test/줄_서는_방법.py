from math import factorial
def solution(n, k):
    lst = list(range(1,n+1))
    ans = []
    k -= 1
    while True:
        n -= 1
        if n == 0:
            ans.append(lst.pop(0))
            break

        x = factorial(n)
        ans.append(lst.pop(k//x))
        k = k%x

    return ans

# print(solution(10,2))