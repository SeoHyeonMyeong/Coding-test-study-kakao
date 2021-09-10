from collections import deque

def solution(numbers):
    s = set()
    q = deque(numbers)
    for i in range(len(numbers)):
        if i == len(numbers)-1:
            break
        num = numbers[i]
        q = deque(numbers[i+1:])
        while q:
            s.add(num + q.popleft())
    
    return list(sorted(s))
numbers = [2,1,3,4,1]
print(solution(numbers))