class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        

        stack = []
        
        for i in range(len(nums)):
            if not stack or nums[stack[-1]]>nums[i]:
                stack.append(i)
        
        max_width = 0
        for i in range(len(nums)-1, -1, -1):
            while stack and nums[i]>=nums[stack[-1]]:
                max_width = max(i-stack.pop(), max_width)

        return max_width
