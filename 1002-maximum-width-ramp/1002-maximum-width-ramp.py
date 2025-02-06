class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        
        l = []

        for i in range(len(nums)):
            l.append((i, nums[i]))

        l.sort(key = lambda x:x[1])

        minVal, maxWidth = float('inf'), 0

        for (i, j) in l:
            maxWidth = max(i-minVal, maxWidth)
            minVal = min(i, minVal)

        return maxWidth
