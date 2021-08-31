def max(arr):
    max_num = arr[0]
    for num in arr:
        if num >= max_num:
            max_num = num
    return max_num

def solution(n, works):
    ans = 0
    for i in range(n):
        works[works.index(max(works))] -= 1
    for num in works:
        ans += num ** 2
    return ans

print(solution(4, [4,3,3]))