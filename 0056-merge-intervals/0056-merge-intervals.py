class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda x:x[0])
        
        res = []
        max_end = intervals[0][1]
        
        res.append([intervals[0][0], intervals[0][1]])
        for start, end in intervals[1:]:
            if start<=max_end: 
                max_end = max(end, max_end)
                res[-1][1] = max_end
            if start>max_end:    
                max_end = end
                res.append([start, end])

        return res