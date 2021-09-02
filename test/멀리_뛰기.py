# Dynamic Programming

memo = []
memo.append(1)
memo.append(1)

def solution(n):
    global memo
    if len(memo)>n:
        return memo[n]
    else:
        for i in range(len(memo),n+1):
            memo.append(memo[i-1] + memo[i-2])
            memo[i] = memo[i]%1234567
    return memo[n]

print(solution(6))