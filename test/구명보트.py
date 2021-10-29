from collections import deque

def solution(people, limit):
    ans = 0
    people.sort()
    people = deque(people)
    while len(people) > 1:
        big = people.pop()
        small = people.popleft()
        if big + small > limit:
            people.appendleft(small)
            ans +=1
        else:
            people.append(big + small)

    return ans + len(people)

# p = [70,50,80,50]
# l = 100
# print(solution(p,l))