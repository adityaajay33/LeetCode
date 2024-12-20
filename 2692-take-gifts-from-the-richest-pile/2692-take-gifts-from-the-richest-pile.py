class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        res = [-gift for gift in gifts]
        heapq.heapify(res)
        for _ in range(k):
            largest = -heapq.heappop(res)
            updated = math.floor(largest ** 0.5)
            heapq.heappush(res, -updated)
        return -sum(res)
        