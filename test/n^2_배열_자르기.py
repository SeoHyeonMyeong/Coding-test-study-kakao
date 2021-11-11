def solution(n, left, right):
    ans = []
    for i in range(left,right+1):
        x = int(i/n) + 1 
        y = i%n + 1
        if x < y:
            ans.append(y)
        else:
            ans.append(x)
    return ans

# n = 3
# l = 2
# r = 5

# print(solution(n,l,r))
