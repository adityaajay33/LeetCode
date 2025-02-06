class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        currSum, maxSum = 0, float('-inf')

        for num in nums:
            
            currSum += num
            maxSum = max(currSum, maxSum)
            
            if currSum<0:
                currSum=0

        return maxSum