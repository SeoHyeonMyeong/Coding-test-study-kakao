def process(num):
    if num % 2 == 0:
        return int(num/2)
    else:
        return num * 3 +1

def work(num):
    if num == 1:
        return 0
    for i in range(500):
        num = process(num)
        if num == 1:
            return i+1
    return -1

def solution(num):
    answer = work(num)
    return answer

print(work(626331))