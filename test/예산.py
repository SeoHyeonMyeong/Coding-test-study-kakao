def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        budget -= d[i]
        if budget <0:
            return i
    return len(d)

d = [1,3,2,5,4]
budget = 9
print(solution(d,budget))