from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        maxSum = 0
        currSum = 0
        elements = {}
        l = 0
        
        for r in range(len(nums)):
            # Add current number to the window
            currSum += nums[r]
            elements[nums[r]] = elements.get(nums[r], 0) + 1
            
            # If the window size exceeds k, shrink it
            if r - l + 1 > k:
                elements[nums[l]] -= 1
                if elements[nums[l]] == 0:
                    del elements[nums[l]]
                currSum -= nums[l]
                l += 1
            
            # Check if the window size is k and contains unique elements
            if r - l + 1 == k and len(elements) == k:
                maxSum = max(maxSum, currSum)
        
        return maxSum