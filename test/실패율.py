def solution(N, stages):
    reach = len(stages)
    failed = [0] * (N+1)
    ans = []

    for person in stages:
        failed[person-1] += 1
    
    for i in range(N):
        if reach == 0:
            ans.append([i+1,0])
        else:
            ans.append([i+1,failed[i]/reach])
            reach -= failed[i]
    ans.sort(reverse=True,key=lambda x:x[1])
    return list(zip(*ans))[0]

# N = 5
# stages = [2, 1, 2, 6, 2, 4, 3, 3]	
# print(solution(N,stages))