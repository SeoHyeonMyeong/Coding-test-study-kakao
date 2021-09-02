def solution(arr):
    memo = arr[0]
    ans = []
    for num in arr:
        if num == memo:
            continue
        else:
            ans.append(memo)
            memo = num
    ans.append(memo)
    return ans

print(solution([1,1,3,3,0,1,1]))