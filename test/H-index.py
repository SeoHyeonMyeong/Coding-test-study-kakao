def solution(citations):
    n = len(citations)
    citations.sort()
    
    ans = 0
    h = n
    while ans == 0 and h > 0:
        if citations[n-h]>=h:
            ans = h
        h -= 1

    return ans

# c = [0]
# print(solution(c))