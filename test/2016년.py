month = [31,29,31,30,31,30,31,31,30,31,30,31]
day = ["THU","FRI","SAT","SUN","MON","TUE","WED"]

def solution(a, b):
    d = 0
    for i in range(0,a-1):
        d += month[i]
    d += b
    d %= 7
    return day[d]

# print(solution(2,1))