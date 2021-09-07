def solution(nums):
    n = len(nums)
    kind = len(set(nums))
    if kind < int(n/2):
        return kind
    return int(n/2)