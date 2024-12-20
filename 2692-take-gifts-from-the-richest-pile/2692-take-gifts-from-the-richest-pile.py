class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        
        res = [-gift for gift in gifts]
        heapq.heapify(res)

        for i in range(k):
            res[0] = -1*(math.floor((-1*res[0])**0.5))
            heapq.heapify(res)

        return -1*sum(res)
        