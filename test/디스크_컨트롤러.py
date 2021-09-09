import heapq

def solution(jobs):
    jobs.sort(reverse=True,key=lambda x:x[0])
    heap = []
    ans = 0
    time = 0
    n = len(jobs)
    
    while len(jobs) > 0 or len(heap) > 0:
        while len(jobs) > 0  and jobs[-1][0] <= time:
            job = jobs.pop()
            ans -= job[0]
            heapq.heappush(heap,job[1])
        if len(heap) == 0:
            job = jobs.pop()
            time = job[0]
            ans -= job[0]
            heapq.heappush(heap,job[1])
        time += heapq.heappop(heap)
        ans += time
    
    return int(ans/n)



jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))