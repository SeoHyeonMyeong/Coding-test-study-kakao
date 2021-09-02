import heapq

heap = []

def solution(n, works):
    ans = 0
    max_heap = []
    for item in works:
        heapq.heappush(max_heap, (-item, item))
    
    for i in range(n):
        max_item = heapq.heappop(max_heap)[1]
        if max_item == 0:
            break
        max_item -= 1
        heapq.heappush(max_heap, (-max_item, max_item))
    
    ans = sum([i[1]**2 for i in max_heap])
    return ans

print(solution(3, [1,1,3,4]))