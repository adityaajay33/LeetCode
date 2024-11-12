class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort(key = lambda x: x[0])

        l1 = []
        l2 = []

        for x, y in items:
            l1.append(x)
            l2.append(y)

        max_to_index = []
        current_max = 0
        for value in l2:
            current_max = max(current_max, value)
            max_to_index.append(current_max)

        res = []
        for query in queries:
            ind = bisect.bisect_right(l1, query)
            res.append(max_to_index[ind-1] if ind>0 else 0)

        return res