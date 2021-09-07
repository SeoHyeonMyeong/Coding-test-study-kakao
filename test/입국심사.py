
def solution(n, times):
    times.sort()
    right = n * times[0]
    left = times[0]
    mid = int((left + right) /2)

    while right != left:
        num = 0
        for time in times:
            num += int(mid/time)
        if num >= n:
            right = mid
        else:
            left = mid+1
        mid = int((left + right) / 2)
        print(left,mid,right)
    return right

solution(3,[1,2,3])