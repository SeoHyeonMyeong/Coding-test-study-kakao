def max(arr):
    max_num = arr[0]
    for num in arr:
        if num >= max_num:
            max_num = num
    return max_num

def solution(n, works):
    ans = 0
    for i in range(n):
        if max(works) == 0:
            break
        works[works.index(max(works))] -= 1
    ans = sum([i**2 for i in works])
    return ans

print(solution(3, [1,1]))