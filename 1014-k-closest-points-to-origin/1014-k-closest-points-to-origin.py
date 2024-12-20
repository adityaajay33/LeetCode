class Solution:
    def euclidean(self, x, y):
        return (pow(x, 2) + pow(y, 2))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for (x, y) in points:
            output = self.euclidean(x, y)
            heapq.heappush(res, (output, (x, y)))

        return [point for _, point in heapq.nsmallest(k, res)]
        