def solution(prices):
    ans = []
    for i in range(len(prices)):
        price = prices[i]
        for j in range(i+1,len(prices)):
            if prices[j]<price:
                ans.append(j-i)
                break
            if j == len(prices) - 1:
                ans.append(j-i)
    return ans + [0]

# print(solution([1,2,3,2,3]))