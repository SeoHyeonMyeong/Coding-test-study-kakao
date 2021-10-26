import copy

def solution(k, dungeons):
    return explore(0,k,dungeons)

def explore(n, k, dungeons):
    ans = n
    for i in range(len(dungeons)):
        need, cost = dungeons[i]
        if k >= need:
            new_dun = copy.deepcopy(dungeons)
            new_dun.pop(i)
            result = explore(n+1, k-cost, new_dun)
            if result > ans:
                ans = result
    return ans

# k = 80
# dun = [[80,20], [50,40], [30,10]]
# print(solution(k,dun))