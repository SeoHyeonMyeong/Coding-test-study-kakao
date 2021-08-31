def solution(n):
    count = 0
    for i in range(1,int(n/2)+1):
        num = i
        sum = num
        while sum < n:
            num += 1
            sum += num
        if sum == n:
            count += 1
    return count + 1

print(solution(15))