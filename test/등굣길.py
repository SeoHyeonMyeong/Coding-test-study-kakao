dp = dict()
def solution(m, n, puddles):
    global dp
    
    for x,y in puddles:
        key = str(x) + "," + str(y)
        dp[key] = 0
    dp["1,1"] = 1
    
    return find(m,n)

def find(m,n):
    global dp
    key = str(m) + "," + str(n)
    if key in dp:
        return dp[key]

    left = 0
    up = 0

    if m > 1:
        left = find(m-1,n)
    if n > 1:
        up = find(m,n-1)

    dp[key] = left+up % 1000000007
    return dp[key]

# m = 4
# n = 3
# pud = [[2,2]]
# print(solution(m,n,pud))