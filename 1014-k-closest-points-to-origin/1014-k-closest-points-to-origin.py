class Solution:
    def euclidean(self, x, y):
        return (pow(x, 2) + pow(y, 2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        res = []

        for (x, y) in points:
            output = self.euclidean(x, y)
            ind = bisect.bisect_left(res, (output, (x, y)))
            if ind<k:
                res.insert(ind, (output, (x, y)))

        return [res[i][1] for i in range(k)]
        