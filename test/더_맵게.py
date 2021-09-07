import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    ans = 0
    while scoville[0] < K:
        ans += 1
        if len(scoville)<2:
            return -1
        item = heapq.heappop(scoville)
        item += heapq.heappop(scoville) * 2
        heapq.heappush(scoville,item)
    return ans