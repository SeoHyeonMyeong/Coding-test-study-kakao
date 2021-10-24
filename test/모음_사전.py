def solution(word):
    indices = ["A","E","I","O","U"]

    n = 5
    weights = []
    weight = 0
    for i in range(n):
        weight = weight * 5 + 1
        weights = [weight] + weights
    
    ans = 0
    for i in range(len(word)):
        ans += indices.index(word[i]) * weights[i] + 1
    return ans

print(solution("UUUUU"))

