first = [1,2,3,4,5]
second = [2,1,2,3,2,4,2,5]
third = [3,3,1,1,2,2,4,4,5,5]

def solution(answers):
    n = len(answers)
    point = [0,0,0]
    for i in range(n):
        answer = answers[i]
        if answer == first[i%len(first)]:
            point[0] += 1
        if answer == second[i%len(second)]:
            point[1] += 1
        if answer == third[i%len(third)]:
            point[2] += 1

    ans = []
    high_point = max(point)
    for i in range(3):
        if point[i] == high_point:
            ans.append(i+1)
    return ans

answers = [1,3,2,4,2]
print(solution(answers))